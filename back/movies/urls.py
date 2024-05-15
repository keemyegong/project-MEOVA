from django.urls import path
from . import views

urlpatterns = [
    # path('meova/search/',views.search), # 영화 검색
    # path('movies/popular/',views.popular), # 인기 영화 조회
    # path('movies/recommended/',views.recommended), # 추천 영화 조회
    # path('movies/release/',views.release), # 최신 영화 조회
    # path('movies/<int:movie_pk>/',views.detail), # 영화 상세 정보 조회
    path('movies/<int:movie_pk>/reviews/', views.reviews), # 리뷰 생성
    # path('movies/<int:movie_pk>/<int:review_pk>/', views.review_detail), # 리뷰 상세 정보 조회, 수정, 삭제
    # path('movies/<int:movie_pk>/<int:review_pk>/comments/', views.comments), # 리뷰 코멘트 생성
    # path('movies/<int:movie_pk>/<int:review_pk>/<int:comment_pk>/', views.comment_detail), # 리뷰 코멘트 삭제
    # path('movies/<int:movie_pk>/tag-comments/', views.tag_comments), # 태그 코멘트 조회, 생성
    # path('movies/<int:movie_pk>/tag-comments/<int:tag_comment_pk>/', views.tag_comment_detail), # 태그 코멘트 삭제
    # path('movies/actors/<int:actor_pk>/', views.actors), # 영화 배우 상세 정보 조회
    # path('movies/directors/<int:director_pk>/', views.directors), # 영화 감독 상세 정보 조회
]
