from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from frontend.views import homepage_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', homepage_api, name='homepage'),

    # user views
    path('api/token/', TokenObtainPairView.as_view(), name='auth'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/exercises/', include('exercises.api.urls')),

    path('api/workouts/', include('workouts.api.urls')),
    path('api/accounts/', include('accounts.api.urls')),
]
