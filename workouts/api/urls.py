from django.urls import path

from .views import (homepage_workout_view, WorkoutListApiView, WorkOutCreateApiView, WorkOutUpdateDeleteRetrieveApiView,
                    WorkoutPartCreateView, WorkoutPartListView, WorkoutPartUpdateView
                    )
app_name = 'workout'


urlpatterns = [
    path('', homepage_workout_view, name='homepage'),
    path('list/', WorkoutListApiView.as_view(), name='list'),
    path('create/', WorkOutCreateApiView.as_view(), name='create'),
    path('retrieve-update-delete/<int:pk>/', WorkOutUpdateDeleteRetrieveApiView.as_view(), name='detail'),
    path('workout-part/create/', WorkoutPartCreateView.as_view(), name='workout_part_create'),
    path('workout-part/list/', WorkoutPartListView.as_view(), name='workout_part_list'),
    path('workout-parts/update/<int:pk>/', WorkoutPartUpdateView.as_view(), name='workout_part_update'),

]




