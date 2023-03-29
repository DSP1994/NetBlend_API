from django.urls import path
from . import views


urlpatterns = [
    path('article/', views.ArticleList.as_view()),
    path('article/<int:pk>/', views.ArticleDetail.as_view()),
]
