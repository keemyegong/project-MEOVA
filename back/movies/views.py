from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Review
from .serializers import MovieListSerializer,MovieSerializer
# Create your views here.

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
    
