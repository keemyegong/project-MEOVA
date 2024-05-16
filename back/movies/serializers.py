from rest_framework import serializers
from .models import Movie,Genre,Keyword,Actor,Director

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
        read_only_fields=('directors','liked_users',)
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields='__all__'
        
class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Keyword
        fields='__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields='__all__'
        read_only_fields=('liked_users',)

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Director
        fields='__all__'
        read_only_fields=('liked_users',)