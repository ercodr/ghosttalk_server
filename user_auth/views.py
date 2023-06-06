from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from user_auth.models import AuthToken
from django.contrib.auth.models import User



@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        try:
            login(request, user)
            if user.is_authenticated:
            # user_instance = User.objects.get(username=username)
            # AuthToken.objects.create(user=user_instance)
            # token = AuthToken.objects.get(user=user).token
                return Response({'is_authenticated': True, 'user': user.get_username() }, status=status.HTTP_200_OK)
            return Response({'is_authenticated': False }, status=status.HTTP_200_OK)
        except Exception as e:
                return Response({'error': e }, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response(
            {'error': 'Invalid username or password.'},
            status=status.HTTP_401_UNAUTHORIZED
        )



@api_view(['POST'])
def create_user(request):
    user = User.objects.filter(username=request.data.get('username'))
    if user:
        return Response(status=status.HTTP_302_FOUND)
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def logout_user(request):
    logout(request)
    return Response({'is_authenticated': False})