from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Dog
from django.contrib.auth.models import User
from .serializers import DogSerializer
from .serializers import UserSerializer

# Create your views here.
class DogsView(generics.ListAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer