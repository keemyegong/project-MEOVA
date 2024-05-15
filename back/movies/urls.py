from django.urls import path
from . import views

urlpatterns = [
    path('meova/search/',views.search),
    path('movies/popular/',views.popular),
    path('movies/recommended/',views.recommended),
    path('movies/release/',views.release),
    path('movies/<int:movie_pk>/',views.detail),
    path('movies/<int:movie_pk>/',views.detail),
]
