from django.contrib import admin
from django.urls import path
from .views import DogsView, UsersView

urlpatterns = [
    path('dogs/', DogsView.as_view()),
    path('users/', UsersView.as_view()),
]