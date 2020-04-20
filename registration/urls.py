from django.urls import path

from registration.views import UserCreate, LoginView
# from rest_framework.authtoken import views


urlpatterns = [
    path("create/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]