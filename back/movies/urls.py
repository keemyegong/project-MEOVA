from django.urls import path
from . import views

urlpatterns = [
    # accounts
    # path('accounts/<int:user_pk>/', views.profile), # 유저 프로필 조회, 탈퇴 
    # path('accounts/<int:user_pk>/settings/', views.profile_settings), # 프로필 수정
    # path('accounts/<int:user_pk>/reviews/', views.user_reviews), # 작성 리뷰 조회
    # path('accounts/<int:user_pk>/comments/', views.user_comments), # 작성 코멘트 조회
    # path('accounts/<int:user_pk>/tag-comments/', views.user_tag_comments), # 작성 태그 코멘트 조회
    # path('accounts/<int:user_pk>/movie-list/<int:movie_list_pk>/', views.user_movie_list), # 유저 추천 영화 리스트
    # path('accounts/<int:user_pk>/follow/', views.follow), # 유저 팔로우/언팔로우
    # path('accounts/<int:user_pk>/follow-list/', views.follow_list), # 유저 팔로우 리스트
    # path('accounts/<int:user_pk>/liked-movies/', views.user_liked_movies), # 유저 좋아요 영화
    # path('accounts/<int:user_pk>/liked-reviews/', views.user_liked_reviews), # 유저 좋아요 리뷰
  
    # movie
    path('',views.get_movie),
    # path('genre/',views.get_genre),
    path('meova/search/',views.search), # 영화 검색
    path('movies/popular/',views.popular), # 인기 영화 조회
    path('movies/recommended/',views.recommended), # 추천 영화 조회
    path('movies/release/',views.release), # 최신 영화 조회
    path('movies/<int:movie_pk>/',views.detail), # 영화 상세 정보 조회
    path('movies/<int:movie_pk>/reviews/', views.reviews), # 리뷰 생성
    path('movies/<int:movie_pk>/<int:review_pk>/', views.review_detail), # 리뷰 상세 정보 조회, 수정, 삭제
    path('movies/<int:movie_pk>/<int:review_pk>/comments/', views.comments), # 리뷰 코멘트 생성
    path('movies/<int:movie_pk>/<int:review_pk>/<int:comment_pk>/', views.comment_detail), # 리뷰 코멘트 삭제
    # path('movies/<int:movie_pk>/tag-comments/', views.tag_comments), # 태그 코멘트 조회, 생성
    # path('movies/<int:movie_pk>/tag-comments/<int:tag_comment_pk>/', views.tag_comment_detail), # 태그 코멘트 삭제
    path('movies/actors/<int:actor_pk>/', views.actor_detail), # 영화 배우 상세 정보 조회
    # path('movies/directors/<int:director_pk>/', views.directors), # 영화 감독 상세 정보 조회
]
