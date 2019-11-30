from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import ExerciseCategory, Exercise
from .api.serializers import ExerciseCategorySerializer, ExerciseSerializer


class ExerciseListApiView(ListAPIView):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.filter(status=True)
    permission_classes = [AllowAny, ]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter )
    filterset_fields = ['category', ]
    search_fields = ['title']


class ExerciseCategoryListApiView(ListAPIView):
    serializer_class = ExerciseCategorySerializer
    queryset = ExerciseCategory.objects.filter(status=True)
    permission_classes = [AllowAny, ]
