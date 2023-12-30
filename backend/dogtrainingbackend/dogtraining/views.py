from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
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

def DogsByOwner(request):
    user_id = request.user.id
    dogs = Dog.objects.filter(owners=user_id)
    data = serializers.serialize('json', dogs)
    return HttpResponse(data)

def OwnersByDog(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    owners = dog.owners.all()
    data = serializers.serialize('json', owners, fields=["username"])
    return HttpResponse(data)