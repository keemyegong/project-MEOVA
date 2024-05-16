from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Review,Credit
from .serializers import MovieListSerializer,MovieSerializer,GenreSerializer,ActorSerializer,DirectorSerializer,KeywordSerializer,WatchProviderSerializer
from django.conf import settings
api_key = settings.TMDB_API_KEY
# Create your views here.

import requests

@api_view(['GET'])
def get_movie(request):
    url = "https://api.themoviedb.org/3/movie/popular?language=ko&page=1"
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"}
    response = requests.get(url,headers=headers).json()
    for movie in response.get('results'):
        id = movie.get('id')
        movie_url = f"https://api.themoviedb.org/3/movie/{id}?language=ko"
        movie_res = requests.get(movie_url,headers=headers).json()
        credit_url = f"https://api.themoviedb.org/3/movie/{id}/credits?language=ko"
        credit_res = requests.get(credit_url,headers=headers).json()
        keyword_url = f"https://api.themoviedb.org/3/movie/{id}/keywords"
        keyword_res = requests.get(keyword_url,headers=headers).json()
        watchprovider_url = f"https://api.themoviedb.org/3/movie/{id}/watch/providers"
        watchprovider_res = requests.get(watchprovider_url,headers=headers).json()
        
        title = movie.get('title')
        overview=movie.get('overview')
        overview = overview if overview else 'none'
        poster_path=movie.get('poster_path')
        vote_average=movie.get('vote_average')
        runtime=movie_res.get('runtime')
        popularity=movie.get('popularity')
        adult=movie.get('adult')
        release_date=movie.get('release_date')
        origin_country=movie_res.get('origin_country')[0]
        genres=movie_res.get('genres')
        save_data = {
            'id': id,
            'title': title,
            'overview': overview,
            'poster_path': poster_path,
            'vote_average': vote_average,
            'popularity': popularity,
            'runtime': runtime,
            'adult': adult,
            'release_date': release_date,
            'origin_country': origin_country,
        }

        serializer = MovieSerializer(data=save_data)
        # 유효성 검증
        if serializer.is_valid():
            # 유효하다면, 저장
            movie_instance = serializer.save()

            # 장르 저장
            for genre in genres:
                serializer = GenreSerializer(data=genre)
                if serializer.is_valid():
                    genre_instance = serializer.save()
                    movie_instance.genres.add(genre_instance)
                    
            for cast in credit_res.get('cast'):
                cast_data={
                    'name':cast.get('name'),
                    'gender':cast.get('gender'),
                    'profile_path':cast.get('profile_path'),
                    'id':cast.get('id'),
                }
                serializer = ActorSerializer(data=cast_data)
                if serializer.is_valid():
                    cast_instance = serializer.save()
                    Credit.objects.create(actor=cast_instance, movie=movie_instance, character=cast.get('character'), order=cast.get('order'))

            directors = [{'name': crew['name'], 'id': crew['id']} for crew in credit_res['crew'] if crew['job'] == 'Director']

            for director_data in directors:
                director_serializer = DirectorSerializer(data=director_data)
                if director_serializer.is_valid():
                    director_instance = director_serializer.save()
                    movie_instance.directors.add(director_instance)
            
            for keyword in keyword_res.get('keywords'):
                serializer = KeywordSerializer(data=keyword)
                if serializer.is_valid():
                    keyword_instance = serializer.save()
                    movie_instance.keywords.add(keyword_instance)
                    
            results = watchprovider_res.get('results')
            if results:
                # 'KR' 키가 존재하는지 확인
                kr_watchprovider = results.get('KR')
                if kr_watchprovider:
                    # 'flatrate' 키가 존재하고 리스트인지 확인
                    flatrate = kr_watchprovider.get('flatrate')
                    if flatrate and isinstance(flatrate, list):
                        for watchprovider in flatrate:
                            # watchprovider를 처리하는 기존 로직
                            watchprovider_data={
                                'name':watchprovider.get('provider_name'),
                                'display_priority':watchprovider.get('display_priority'),
                                'logo_path':watchprovider.get('logo_path'),
                                'id':watchprovider.get('provider_id'),
                            }
                            
                            serializer = WatchProviderSerializer(data=watchprovider_data)
                            if serializer.is_valid():
                                watchprovider_instance = serializer.save()
                                movie_instance.watchproviders.add(watchprovider_instance)
        
    return Response(response)

@api_view(['GET'])
def get_genre(request):
    url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"}
    response = requests.get(url,headers=headers).json()
    
    for genre in response.get('genres'):
        # 원하는 데이터 추출하기
        pk = genre.get('id')
        name = genre.get('name')

        save_data = {
            'id': pk,
            'name': name,
        }

        serializer = GenreSerializer(data=save_data)
        # 유효성 검증
        if serializer.is_valid(raise_exception=True):
            # 유효하다면, 저장
            serializer.save()

    return Response(response)

def get_people(request):
    movies = Movie.objects.all()
    


@api_view(['GET'])
def search(request):
    if request.method=='GET':
        query=request.GET.get('q')
        if query:
            movies=Movie.objects.filter(title__contains=query)
        else:
            movies=Movie.objects.all()
        serializer=MovieListSerializer(movies,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET'])
def popular(request):
    if request.method=="GET":
        movies=Movie.objects.all().order_by('-popularity')
        serializer=MovieListSerializer(movies,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
@api_view(['GET'])
def recommended(request):
    ...

    
@api_view(['GET'])
def release(request):
    if request.method=="GET":
        movies=Movie.objects.all().order_by('-release_date')
        serializer=MovieListSerializer(movies,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
@api_view(['GET'])
def detail(request,movie_pk):
    if request.method=="GET":
        movie=get_object_or_404(Movie,pk=movie_pk)
        serializer=MovieSerializer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
