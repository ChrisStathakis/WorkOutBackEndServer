from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from .serializers import WorkOutPartSerializer, WorkOutSerializer, WorkOutCreateSerializer

from ..models import WorkOut, WorkOutParts
from .permissions import IsOwnerOrReadOnly


@api_view(['GET', ])
def homepage_workout_view(request, format=None):
    return Response({
        'workouts': reverse('workout:list', format=None, request=request),
        'create_workout': reverse('workout:create', format=None, request=request)
    })


class WorkoutListApiView(ListAPIView):
    serializer_class = WorkOutSerializer
    queryset = WorkOut.objects.all()
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_queryset(self):
        user = self.request.user
        if not user:
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
    serializer_class = WorkOutSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return WorkOut.objects.filter(public=True)
        user_qs = WorkOut.objects.filter(user_related=user)
        public_qs = WorkOut.objects.filter(public=True, status=True)
        return user_qs | public_qs

