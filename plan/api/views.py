from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PlannerWorkoutSerializer, PlannerSerializer, PlannerDetailSerializer, PlannerWorkoutDetailSerializer
from ..models import Planner, PlannerWorkOut


@api_view(['GET', ])
def planner_homepage_view(request, format=None):
    return Response({
        'planners': reverse('planner:list', format=None, request=request),
        'planner-workouts': reverse('planner:workouts_list', format=None, request=request)
    })


class PlannerListView(ListCreateAPIView):
    serializer_class = PlannerSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['active', ]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Planner.objects.filter(user=user)
        return Planner.objects.none()


class PlannerUpdateApiListView(RetrieveUpdateDestroyAPIView):
    serializer_class = PlannerDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Planner.objects.filter(user=user)
        return Planner.objects.none()


class PlannerWorkOutApiListView(ListCreateAPIView):
    serializer_class = PlannerWorkoutSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['is_done', 'workout']

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return PlannerWorkOut.objects.filter(planner_related__user=user)
        return PlannerWorkOut.objects.none()


class PlannerWorkoutUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = PlannerWorkoutDetailSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return PlannerWorkOut.objects.filter(planner_related__user=user)
        return PlannerWorkOut.objects.none()