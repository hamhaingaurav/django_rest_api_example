from django.shortcuts import render
from django.contrib.auth.models import User

from example.api.serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

class HomeView(APIView):
    def get(self, request):
        message = {'message':'Hello Gaurav !','status':'Success'}
        return Response(message)


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


@api_view(['GET'])
def user_detail(request, id):
    try:
        user_obj = User.objects.get(pk=id)
        user = {'username': user_obj.username, 
            'is_staff': user_obj.is_staff, 
            'is_superuser': user_obj.is_superuser,
            'email': user_obj.email,
            'status': 'success'
            }
    except Exception:
        user = {'status': 'failed'}
    
    return Response(user)