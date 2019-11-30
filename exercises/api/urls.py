from django.urls import path
from .views import (ExerciseListApiView, ExerciseCategoryListApiView, exercise_homepage_view,
                    ExerciseDetailApiView, ExerciseCategoryRetrieveView
                    )

app_name = 'exercise'

urlpatterns = [
    path('homepage', exercise_homepage_view, name='homepage'),
    path('list/', ExerciseListApiView.as_view(), name='list'),
    path('detail/<int:pk>/', ExerciseDetailApiView.as_view(), name='detail_view'),
    path('category/list/', ExerciseCategoryListApiView.as_view(), name='category_list'),
    path('category/detail/<int:pk>/', ExerciseCategoryRetrieveView.as_view(), name='category_detail')
]
