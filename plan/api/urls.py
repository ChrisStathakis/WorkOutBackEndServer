from django.urls import path
from .views import (planner_homepage_view, PlannerListView, PlannerWorkOutApiListView
                    , PlannerUpdateApiListView, PlannerWorkoutUpdateApiView
                    )

app_name = 'planner'

urlpatterns = [
    path('homepage/', planner_homepage_view, name='homepage'),
    path('list/', PlannerListView.as_view(), name='list'),
    path('update/<int:pk>/', PlannerUpdateApiListView.as_view(), name='detail'),
    path('workouts/list/', PlannerWorkOutApiListView.as_view(), name='workouts_list'),
    path('workouts/update/<int:pk>/', PlannerWorkoutUpdateApiView.as_view(), name='workout_detail')
]
