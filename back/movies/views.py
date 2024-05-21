from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Review, Credit, Actor, ReviewComment, Director, TagComment
from .serializers import MovieListSerializer,MovieSerializer,GenreSerializer,ActorSerializer,DirectorSerializer,KeywordSerializer,WatchProviderSerializer,ReviewSerializer,ReviewCommentSerializer,TagCommentSerializer, ChatGPTSerializer
from django.conf import settings
from django.db.models import Q
api_key = settings.TMDB_API_KEY

# Create your views here.

import requests

@api_view(['GET'])
def get_movie(request):
    for i in range(1,21):
        url = f"https://api.themoviedb.org/3/movie/popular?language=ko&page={i}"
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
            if overview:
                overview = overview
            else:
                en_url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
                en_res = requests.get(en_url,headers=headers).json()
                overview=en_res.get('overview')
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
                        
                for index, cast in enumerate(credit_res.get('cast')):
                    if index >= 5:
                        break  # 처음 5명의 배우만 처리하고 루프 종료

                    # 배우 ID로 기존 배우 검색
                    existing_actor = Actor.objects.filter(id=cast.get('id')).first()

                    if existing_actor:
                        # 기존 배우가 있는 경우 기존 배우를 사용하여 Credit 생성
                        Credit.objects.create(
                            actor=existing_actor,
                            movie=movie_instance,
                            character=cast.get('character'),
                            order=cast.get('order')
                        )
                    else:
                        # 기존 배우가 없는 경우 새로운 배우를 생성하여 Credit 생성
                        cast_data = {
                            'name': cast.get('name'),
                            'gender': cast.get('gender'),
                            'profile_path': cast.get('profile_path'),
                            'id': cast.get('id'),
                        }
                        serializer = ActorSerializer(data=cast_data)
                        if serializer.is_valid():
                            cast_instance = serializer.save()
                            Credit.objects.create(
                                actor=cast_instance,
                                movie=movie_instance,
                                character=cast.get('character'),
                                order=cast.get('order')
                            )

                directors = [{'name': crew['name'], 'id': crew['id']} for crew in credit_res['crew'] if crew['job'] == 'Director']

                for director_data in directors:
                    # 감독 ID로 기존 감독 검색
                    existing_director = Director.objects.filter(id=director_data['id']).first()

                    if existing_director:
                        # 기존 감독이 있는 경우 기존 감독을 사용하여 Movie에 추가
                        movie_instance.directors.add(existing_director)
                    else:
                        # 기존 감독이 없는 경우 새로운 감독 생성 후 Movie에 추가
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
def search(request):
    if request.method=='GET':
        title_query = request.GET.get('title')
        genre_query = request.GET.get('genre')
        keyword_query = request.GET.get('keyword')
        runtime_query = request.GET.get('runtime')
        country_query = request.GET.get('country')

        movies = Movie.objects.all()
        if title_query:
            movies = movies.filter(title__icontains=title_query)
        if genre_query:
            movies = movies.filter(genres__name__icontains=genre_query)
        if keyword_query:
            movies = movies.filter(keywords__name__icontains=keyword_query)
        if country_query:
            movies = movies.filter(origin_country__icontains=country_query)
        if runtime_query:
            if runtime_query == 'under_1_hour':
                movies = movies.filter(runtime__lte=60)
            elif runtime_query == 'under_2_hours':
                movies = movies.filter(runtime__lte=120)
            elif runtime_query == 'under_3_hours':
                movies = movies.filter(runtime__lte=180)
            elif runtime_query == 'over_3_hours':
                movies = movies.filter(runtime__gt=180)

        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
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
@permission_classes([IsAuthenticated])
def detail(request, movie_pk):
    if request.method=="GET":
        movie=get_object_or_404(Movie,pk=movie_pk)
        serializer=MovieSerializer(movie,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_movie(request, movie_pk):
    movie=get_object_or_404(Movie,pk=movie_pk)
    if request.method=="POST":
        if request.user in movie.liked_users.all():
            movie.liked_users.remove(request.user)
        else:
            movie.liked_users.add(request.user)
        serializer=MovieSerializer(movie,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def actor_detail(request, actor_pk):
    if request.method == 'GET':
        actor = get_object_or_404(Actor, pk=actor_pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_actor(request, actor_pk):
    actor=get_object_or_404(Actor,pk=actor_pk)
    if request.method=="POST":
        if request.user in actor.liked_users.all():
            actor.liked_users.remove(request.user)
        else:
            actor.liked_users.add(request.user)
        serializer=MovieSerializer(actor,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])   
def reviews(request,movie_pk):
    movie=get_object_or_404(Movie,pk=movie_pk)
    if request.method=='POST':
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user,movie=movie)
            return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_review(request, review_pk):
    review=get_object_or_404(Review,pk=review_pk)
    if request.method=="POST":
        if request.user in review.liked_users.all():
            review.liked_users.remove(request.user)
        else:
            review.liked_users.add(request.user)
        serializer=ReviewSerializer(review,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])   
def reviewlist(request,user_pk):
    reviews=Review.objects.filter(user=user_pk)
    if request.method=='GET':
        serializer=ReviewSerializer(reviews,many=True)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])  
def review_detail(request, review_pk):
    review=get_object_or_404(Review,pk=review_pk)
    if request.method=='PUT':
        serializer=ReviewSerializer(review,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method=='GET':
        serializer=ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='DELETE'and review.user==request.user:
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])   
def comments(request, review_pk):
    review=get_object_or_404(Review,pk=review_pk)
    if request.method=='POST':
        serializer=ReviewCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user,review=review)
            return Response(serializer.data)
        
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    comment=get_object_or_404(ReviewComment,pk=comment_pk)
    if request.method=='DELETE' and comment.user==request.user:
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def director_detail(request, director_pk):
    if request.method == 'GET':
        director = get_object_or_404(Director, pk=director_pk)
        serializer = DirectorSerializer(director)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_director(request, director_pk):
    director=get_object_or_404(Director,pk=director_pk)
    if request.method=="POST":
        if request.user in director.liked_users.all():
            director.liked_users.remove(request.user)
        else:
            director.liked_users.add(request.user)
        serializer=MovieSerializer(director,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tag_comments(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = TagCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def tag_comment_detail(request, tag_comment_pk):
    tag_comment = get_object_or_404(TagComment, pk=tag_comment_pk)
    if request.method=='DELETE'and tag_comment.user==request.user:
        tag_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Chat GPT
# views.py
import os
from openai import OpenAI
from django.http import JsonResponse
client = OpenAI(api_key=settings.OPENAI_API_KEY)
info = {}

@api_view(['GET'])
def chat_gpt(request):
    # 데이터베이스에서 영화 정보 가져오기
    movies = Movie.objects.all()
    # movie_list = "\n".join([f"{movie.title} ({movie.genre}): {movie.overview}" for movie in movies])
    # prompt = f"Based on the following movies, recommend a movie for someone who likes action and comedy:\n{movie_list}"
    prompt = 'hi!'
    
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "너는 영화 추천을 위한 chatbot이고 한글로 꼭 대답해야해."},
        # {"role": "system", "content": "답변을 할 때 이 정보를 기반해서 알려줘 {info}"},
        {"role": "user", "content": f"{prompt}"},
        # {"role": "user", "content": f"{prompt}"}
    ]
    )
    
    response = openai.Completion.create(
        engine="gpt-4o",
        prompt=prompt,
        # max_tokens=100
    )
    message = completion.choices[0].message
    
    return Response(message, status=status.HTTP_204_NO_CONTENT)
    
    # recommendations = response.choices[0].text.strip()
    # return JsonResponse({'recommendations': recommendations})