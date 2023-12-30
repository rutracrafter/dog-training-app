from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
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

@permission_classes([IsAuthenticated])
def DogsByOwner(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'User not authenticated'}, status=401)

        user_id = request.user.id
        dogs = Dog.objects.filter(owners=user_id)
        data = serializers.serialize('json', dogs)
        return HttpResponse(data)
    else:
        return HttpResponse(f'Invalid HTTP method: {request.method}')

def OwnersByDog(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    owners = dog.owners.all()
    data = serializers.serialize('json', owners, fields=["username"])
    return HttpResponse(data)