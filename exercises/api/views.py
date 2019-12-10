from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from ..models import ExerciseCategory, Exercise
from .serializers import ExerciseCategorySerializer, ExerciseSerializer, ExerciseRetrieveSerializer


@api_view(['GET'])
def exercise_homepage_view(request, format=None):
    return Response({
        'exercises': reverse('exercise:list', format=None, request=request),
        'categories': reverse('exercise:category_list', format=None, request=request)
    })


class ExerciseListApiView(ListAPIView):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.filter(status=True)
    permission_classes = [AllowAny, ]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['category', ]
    search_fields = ['title']


class ExerciseDetailApiView(RetrieveAPIView):
    serializer_class = ExerciseRetrieveSerializer
    queryset = Exercise.objects.filter(status=True)
    permission_classes = [AllowAny, ]


class ExerciseCategoryListApiView(ListAPIView):
    serializer_class = ExerciseCategorySerializer
    queryset = ExerciseCategory.objects.filter(status=True)
    permission_classes = [AllowAny, ]


class ExerciseCategoryRetrieveView(RetrieveAPIView):
    serializer_class = ExerciseCategorySerializer
    queryset = ExerciseCategory.objects.filter(status=True)
    permission_classes = [AllowAny, ]