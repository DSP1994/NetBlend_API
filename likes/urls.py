from django.urls import path
from likes import views

urlpattern = [
    path('likes/', views.LikeList().as_view()),
]