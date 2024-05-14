from django.db import models
from django.conf import settings
# Create your models here.
class Director(models.Model):
    liked_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_directors')
    name=models.CharField(max_length=50)

class Actor(models.Model):
    liked_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_actors')
    name=models.CharField(max_length=50)
    profile_path=models.CharField(max_length=50)
    gender=models.IntegerField()

class Genre(models.Model):
    liked_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_genres')
    category=models.CharField(max_length=50)
    
class Movie(models.Model):
    liked_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_movies')
    director=models.ForeignKey(Director,on_delete=models.SET_NULL)
    title=models.CharField(max_length=100)
    overview=models.TextField()
    poster_path=models.CharField(max_length=50)
    vote_average=models.DecimalField(max_digits=4,decimal_places=3)
    runtime=models.IntegerField()
    adult=models.BooleanField()
    origin_country=models.CharField(max_length=50)
    genres=models.ManyToManyField(Genre, related_name='movies')
    actors=models.ManyToManyField(Actor,related_name='movies',through='Credit')

class Credit(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.SET_NULL)
    actor=models.ForeignKey(Actor,on_delete=models.SET_NULL)
    character=models.CharField(max_length=100)
    
class SelectedList(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    movies=models.ManyToManyField(Movie,related_name='selected-lists')
    title=models.CharField(max_length=100)
    overview=models.TextField()
    
class Review(models.Model):
    liked_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_reviews')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    vote=models.DecimalField(max_digits=2,decimal_places=1)
    title=models.CharField(max_length=100)
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
