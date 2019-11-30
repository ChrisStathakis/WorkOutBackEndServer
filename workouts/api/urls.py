from django.urls import path

from .views import homepage_workout_view, WorkoutListApiView, WorkOutCreateApiView, WorkOutUpdateDeleteRetrieveApiView
app_name = 'workout'


urlpatterns = [
    path('', homepage_workout_view, name='homepage'),
    path('list/', WorkoutListApiView.as_view(), name='list'),
    path('create/', WorkOutCreateApiView.as_view(), name='create'),
    path('retrieve-update-delete/<int:pk>/', WorkOutUpdateDeleteRetrieveApiView.as_view(), name='detail')

]




