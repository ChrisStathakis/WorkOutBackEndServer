from django.urls import path
from .views import get_current_user_api_view, UserCreateApiView, account_homepage

app_name = 'accounts'

urlpatterns = [
    path('homepage/', account_homepage, name='homepage'),
    path('current-user/', get_current_user_api_view, name='current_user_view'),
    path('create/user/', UserCreateApiView.as_view(), name='create_user')
    ]