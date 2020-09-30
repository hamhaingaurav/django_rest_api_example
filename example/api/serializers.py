from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'first_name', 'last_name', 'username', 'email', 'is_superuser', 'is_staff', 'is_active', 'date_joined']
        # fields = '__all__'
