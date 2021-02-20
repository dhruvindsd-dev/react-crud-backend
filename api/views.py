from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserSeralizer
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['POST'])
def add(request):
    data = request.data
    if 'username' in data and 'password' in data:
        # create user
        User.objects.create_user(
            username=data['username'], password=data['password'])
        return Response('created user')
    else:
        return Response('invalid fields')


@api_view(['DELETE'])
def remove(request):
    data = request.GET
    if 'username' in data:
        try:
            user = User.objects.get(username=data['username'])
        except:
            return Response('no such user found')
        else:
            user.delete()
            return Response('user deleted')
    else:
        return Response('invalid fields')


@api_view(['PATCH'])
def edit(request):
    data = request.data
    if 'username' in data and 'newUsername' in data:
        try:
            user = User.objects.get(username=data['username'])
        except:
            return Response('no user exists')
        else:
            user.username = data['newUsername']
            user.save()
            return Response('success')
    else:
        return Response('invalid fields')


@api_view(['GET'])
def get(request):
    users = User.objects.all()
    users = UserSeralizer(users, many=True)
    return Response(users.data)
