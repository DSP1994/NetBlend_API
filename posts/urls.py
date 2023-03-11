from django.urls import path
from posts import views

# url links for posts
urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>', views.PostDetail.as_view()),
]
