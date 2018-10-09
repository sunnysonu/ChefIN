from app.serializers.UserProfile import *
from app.serializers.ChefProfile import *
from django.contrib.auth.models import *
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import *

class UserProfileSignup(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format = None):
        serializer = UserProfileSignupSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, format = None):
        users = UserProfile.objects.all()
        serializer = ProfileSerializer(users, many=True)
        return Response(serializer.data)

class UserDetailProfile(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

class ChefProfileSignup(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = ChefProfileSignupSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        users = ChefProfile.objects.all()
        serializer = ChefProfileSerializer(users, many=True)
        return Response(serializer.data)

class ChefDetailProfile(RetrieveAPIView):
    queryset = ChefProfile.objects.all()
    serializer_class = ChefProfileSerializer