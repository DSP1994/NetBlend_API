from django.urls import path
from profiles import views

# url links for profiles
urlpatterns = [
    path('', views.index, name='index')
]
