from django.shortcuts import render
from django.contrib.auth.models import User
from example.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

# Create your views here.

class HomeView(APIView):
    def get(self, request):
        message = {'message':'Hello Gaurav !','status':'Success'}
        return Response(message)


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()