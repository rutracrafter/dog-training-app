from django.contrib import admin
from django.urls import path
from .views import DogsView, UsersView, DogsByOwner, OwnersByDog

urlpatterns = [
    path('dogs/', DogsView.as_view()),
    path('users/', UsersView.as_view()),
    path('dogs-by-owner/', DogsByOwner),
    path('owners-by-dog/<int:dog_id>', OwnersByDog),
]