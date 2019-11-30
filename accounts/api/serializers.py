from rest_framework import serializers
from rest_framework_simplejwt.settings import  api_settings
from django.contrib.auth import get_user_model
from ..models import Profile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'id', 'email', 'first_name', 'last_name')


def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields =['first_name', 'last_name', 'email', 'password', 'username']

    def create(self, validated_data):
        username = validated_data.get('username', None)
        password = validated_data.get('password', None)
        email = validated_data.get('email')
        if username and password and email:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return user
        return None




