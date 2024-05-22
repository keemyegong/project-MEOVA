from rest_framework import serializers
from .models import Movie, Director, Genre,Keyword,Actor,Director,WatchProvider,Credit,Review,ReviewComment, TagComment,AIRecommend

class AIRecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model=AIRecommend
        fields='__all__'

class MovieCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'poster_path')

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
        fields = ('id', 'name',)

class CreditSerializer(serializers.ModelSerializer):
    actor = ActorNameSerializer(read_only=True)
    class Meta:
        model = Credit
        fields = ('actor', 'character',)

        
class ReviewCommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    profile_photo = serializers.ImageField(source='user.profile_photo', read_only=True)
    class Meta:
        model=ReviewComment
        fields='__all__'
        read_only_fields=('user','review',)

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    profile_photo = serializers.ImageField(source='user.profile_photo', read_only=True)
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    reviewcomment_set = ReviewCommentSerializer(read_only=True, many=True)
    movie = MovieCardSerializer(read_only=True)
    class Meta:
        model=Review
        fields='__all__'
        read_only_fields=('user','movie','liked_users',)

class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreNameSerializer(read_only=True,many=True)
    keywords = KeywordNameSerializer(read_only=True,many=True)
    class Meta:
        model=Movie
        exclude=('actors','release_date','popularity',)


class TagCommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    profile_photo = serializers.ImageField(source='user.profile_photo', read_only=True)
    class Meta:
        model = TagComment
        fields = '__all__'
        read_only_fields=('user', 'username', 'nickname', 'profile_photo', 'movie',)

class MovieSerializer(serializers.ModelSerializer):
    directors = DirectorNameSerializer(read_only=True, many=True)
    genres = GenreNameSerializer(read_only=True,many=True)
    keywords = KeywordNameSerializer(read_only=True,many=True)
    credits = CreditSerializer(source='credit_set', many=True, read_only=True)
    tagcomment_set = TagCommentSerializer(read_only=True, many=True)
    review_set = ReviewSerializer(read_only=True, many=True)
    my_reviews = serializers.SerializerMethodField()  # 사용자의 리뷰만 추출
    class Meta:
        model=Movie
        fields='__all__'
        read_only_fields=('directors','liked_users','watchproviders',)
    def get_my_reviews(self, obj):
        request = self.context.get('request', None)
        if request is None or request.user.is_anonymous:
            return []
        user = request.user
        user_reviews = obj.review_set.filter(user=user)
        return ReviewSerializer(user_reviews, many=True).data
        
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
    movies = MovieSerializer(read_only=True, many=True)
    class Meta:
        model=Actor
        fields='__all__'
        read_only_fields=('liked_users',)

class DirectorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(read_only=True, many=True)
    class Meta:
        model=Director
        fields='__all__'
        read_only_fields=('liked_users',)

# Chat GPT
class ChatGPTSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)