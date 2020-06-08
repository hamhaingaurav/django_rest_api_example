from django.urls import path
from example.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/users/', UserListAPIView.as_view(), name='user_listapiview'),
]