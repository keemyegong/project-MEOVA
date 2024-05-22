from django.urls import path
from . import views

urlpatterns = [
    # movie
    path('',views.get_movie),
    path('meova/search/',views.search), # 영화 검색
    path('movies/popular/',views.popular), # 인기 영화 조회
    path('movies/recommended/',views.recommended), # 추천 영화 조회
    path('movies/recommended/<int:movie_pk>/',views.recommendedmovies), # 추천 영화 조회
    path('movies/release/',views.release), # 최신 영화 조회
    path('movies/<int:movie_pk>/',views.detail), # 영화 상세 정보 조회
    path('movies/<int:movie_pk>/like/',views.like_movie), # 영화 좋아요
    path('movies/<int:movie_pk>/reviews/', views.reviews), # 리뷰 생성
    path('reviews/<int:review_pk>/', views.review_detail), # 리뷰 상세 정보 조회, 수정, 삭제
    path('reviews/<int:review_pk>/like/', views.like_review), # 리뷰 상세 정보 조회, 수정, 삭제
    path('<int:user_pk>/reviews/', views.reviewlist), # 리뷰 상세 정보 조회, 수정, 삭제
    path('reviews/<int:review_pk>/comments/', views.comments), # 리뷰 코멘트 생성
    path('comments/<int:comment_pk>/', views.comment_detail), # 리뷰 코멘트 삭제
    path('actors/<int:actor_pk>/', views.actor_detail), # 영화 배우 상세 정보 조회
    path('actors/<int:actor_pk>/like/', views.like_actor), # 영화 배우 상세 정보 조회
    path('directors/<int:director_pk>/', views.director_detail), # 영화 감독 상세 정보 조회
    path('directors/<int:director_pk>/like/', views.like_director), # 영화 감독 상세 정보 조회
    path('movies/<int:movie_pk>/tag-comments/', views.tag_comments), # 태그 코멘트 조회, 생성
    path('tag-comments/<int:tag_comment_pk>/', views.tag_comment_detail), # 태그 코멘트 삭제
    # Chat GPT
    path('chat/', views.chat_gpt),
]
