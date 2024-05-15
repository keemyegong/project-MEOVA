from rest_framework import serializers
from .models import Movie,Genre,Keyword

class GenreNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields=('name',)
        
class KeywordNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Keyword
        fields=('name',)

class MovieListSerializer(serializers.ModelSerializer):
    genres=GenreNameSerializer(read_only=True,many=True)
    keywords=KeywordNameSerializer(read_only=True,many=True)
    class Meta:
        model=Movie
        exclude=('actors','director','release_date','popularity',)
        

class MovieSerializer(serializers.ModelSerializer):
    genres=GenreNameSerializer(read_only=True,many=True)
    keywords=KeywordNameSerializer(read_only=True,many=True)
    class Meta:
        model=Movie
        fields='__all__'
        
