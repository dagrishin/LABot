import os

from django.urls import path

from registration.views import UserCreate, LoginView
# from rest_framework.authtoken import views

app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path("create/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]