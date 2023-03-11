from django.urls import path
from posts import views

# url links for posts
urlpatterns = [
    path('posts/', views.PostList.as_view()),
]
