from rest_framework import serializers
from .models import Dog
from django.contrib.auth.models import User

class DogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dog
        fields = ['photo', 'name', 'age', 'food', 'progress', 'creation_date']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']