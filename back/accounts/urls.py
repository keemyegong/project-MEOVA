from django.urls import path
from . import views

urlpatterns = [
    '''
    path('accounts/<int:user_pk>/', views.profile), # 유저 프로필 조회, 탈퇴
    path('accounts/<int:user_pk>/settings/', views.profile_settings), # 프로필 수정
    path('accounts/<int:user_pk>/reviews/', views.user_reviews), # 작성 리뷰 조회
    path('accounts/<int:user_pk>/comments/', views.user_comments), # 작성 코멘트 조회
    path('accounts/<int:user_pk>/tag-comments/', views.user_tag_comments), # 작성 태그 코멘트 조회
    path('accounts/<int:user_pk>/movie-list/<int:movie_list_pk>/', views.user_movie_list), # 유저 추천 영화 리스트
    path('accounts/<int:user_pk>/follow/', views.follow), # 유저 팔로우/언팔로우
    path('accounts/<int:user_pk>/follow-list/', views.follow_list), # 유저 팔로우 리스트
    path('accounts/<int:user_pk>/liked-movies/', views.user_liked_movies), # 유저 좋아요 영화
    path('accounts/<int:user_pk>/liked-reviews/', views.user_liked_reviews), # 유저 좋아요 리뷰
    '''
]
