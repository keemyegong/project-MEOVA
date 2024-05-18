from rest_framework import serializers
from .models import Movie, Director, Genre,Keyword,Actor,Director,WatchProvider,Credit,Review,ReviewComment

class GenreNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields=('name',)
        
class KeywordNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Keyword
        fields=('name',)

class ActorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'profile_path',)

class DirectorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('name',)

class CreditSerializer(serializers.ModelSerializer):
    actor = ActorNameSerializer(read_only=True)
    class Meta:
        model = Credit
        fields = ('actor', 'character',)
        
class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreNameSerializer(read_only=True,many=True)
    keywords = KeywordNameSerializer(read_only=True,many=True)
    class Meta:
        model=Movie
        exclude=('actors','release_date','popularity',)
        
class MovieSerializer(serializers.ModelSerializer):
    directors = DirectorNameSerializer(read_only=True, many=True)
    genres = GenreNameSerializer(read_only=True,many=True)
    keywords=KeywordNameSerializer(read_only=True,many=True)
    credits = CreditSerializer(source='credit_set', many=True, read_only=True)
    # actors = ActorNameSerializer(read_only=True, many=True)
    class Meta:
        model=Movie
        fields='__all__'
        read_only_fields=('directors','liked_users','watchproviders',)
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields='__all__'
        
class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Keyword
        fields='__all__'
        
class WatchProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model=WatchProvider
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
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'
        read_only_fields=('user','movie','liked_users',)
        
class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReviewComment
        fields='__all__'
        read_only_fields=('user','review',)