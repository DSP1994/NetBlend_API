from django.urls import path
from profiles import views

# url links for profiles
urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view())
]
