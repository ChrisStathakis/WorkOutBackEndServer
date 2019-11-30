from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model

from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import UserSerializer, UserCreateSerializer

User = get_user_model()


@api_view(['GET'])
def account_homepage(request, format=None):
    return Response({
        'current_user': reverse('accounts:current_user_view', format=None, request=request),
        'register_view': reverse('accounts:create_user', format=None, request=request),

    })


@api_view(['GET'])
def get_current_user_api_view(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny, ]
