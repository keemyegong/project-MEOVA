from django.db import models
from django.conf import settings
# Create your models here.
class Director(models.Model):
    id = models.IntegerField(primary_key=True)  # 직접 id 필드 정의
    liked_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_directors')
    name=models.CharField(max_length=50)

class Actor(models.Model):
    id = models.IntegerField(primary_key=True)  # 직접 id 필드 정의
    liked_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_actors')
    name=models.CharField(max_length=50)
    profile_path=models.CharField(max_length=50)
    gender=models.IntegerField()

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)  # 직접 id 필드 정의
    name=models.CharField(max_length=50)
    
class Keyword(models.Model):
    id = models.IntegerField(primary_key=True)  # 직접 id 필드 정의
    name=models.CharField(max_length=50)

class WatchProvider(models.Model):
    id = models.IntegerField(primary_key=True)  # 직접 id 필드 정의
    logo_path=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    display_priority=models.IntegerField()
    
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)  # 직접 id 필드 정의
    liked_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_movies')
    directors=models.ManyToManyField(Director,related_name='movies')
    title=models.CharField(max_length=200)
    overview=models.TextField()
    poster_path=models.CharField(max_length=50)
    vote_average=models.DecimalField(max_digits=5,decimal_places=4)
    runtime=models.IntegerField()
    adult=models.BooleanField()
    origin_country=models.CharField(max_length=50)
    release_date=models.DateField()
    popularity=models.DecimalField(max_digits=10,decimal_places=4)
    genres=models.ManyToManyField(Genre, related_name='movies')
    keywords=models.ManyToManyField(Keyword, related_name='movies')
    actors=models.ManyToManyField(Actor,related_name='movies',through='Credit')
    watchproviders=models.ManyToManyField(WatchProvider,related_name='movies')
    
class Credit(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    actor=models.ForeignKey(Actor,on_delete=models.CASCADE)
    character=models.CharField(max_length=200)
    order=models.IntegerField()
    
class SelectedList(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    movies=models.ManyToManyField(Movie,related_name='selected_lists')
    title=models.CharField(max_length=200)
    overview=models.TextField()
    
class Review(models.Model):
    liked_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_reviews')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    vote=models.DecimalField(max_digits=2,decimal_places=1)
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
class ReviewComment(models.Model):
    review=models.ForeignKey(Review,on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

class TagComment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    content=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

