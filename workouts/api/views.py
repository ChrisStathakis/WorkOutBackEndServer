from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import WorkOutPartSerializer, WorkOutSerializer, WorkOutCreateSerializer, WorkoutDetailSerializer

from ..models import WorkOut, WorkOutParts
from .permissions import IsOwnerOrReadOnly


@api_view(['GET', ])
def homepage_workout_view(request, format=None):
    return Response({
        'workouts': reverse('workout:list', format=None, request=request),
        'create_workout': reverse('workout:create', format=None, request=request),
        'workout-parts': reverse('workout:workout_part_list', format=None, request=request),
        'workout-parts-create': reverse('workout:workout_part_create', format=None, request=request)
    })


class WorkoutListApiView(ListAPIView):
    serializer_class = WorkOutSerializer
    queryset = WorkOut.objects.all()
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return WorkOut.objects.filter(public=True)
        user_qs = WorkOut.objects.filter(user_related=user)
        public_qs = WorkOut.objects.filter(public=True, status=True)
        return user_qs | public_qs


class WorkOutCreateApiView(CreateAPIView):
    serializer_class = WorkOutCreateSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user_related=self.request.user)


class WorkOutUpdateDeleteRetrieveApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutDetailSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return WorkOut.objects.filter(public=True)
        user_qs = WorkOut.objects.filter(user_related=user)
        public_qs = WorkOut.objects.filter(public=True, status=True)
        return user_qs | public_qs


class WorkoutPartListView(ListAPIView):
    serializer_class = WorkOutPartSerializer
    queryset = WorkOutParts.objects.all()
    permissions = [permissions.AllowAny, ]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['exercise_related', 'workout_related']


class WorkoutPartCreateView(CreateAPIView):
    serializer_class = WorkOutPartSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class WorkoutPartUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = WorkOutPartSerializer
    queryset = WorkOutParts.objects.all()
    permission_classes = [IsOwnerOrReadOnly, ]
