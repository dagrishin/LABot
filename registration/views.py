from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from .models import User
from .serializers import UserCreateSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserCreateSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.filter(username=username).first()
        if user:
            if user.is_active:
                user = authenticate(username=username, password=password)
                return Response({"token": user.auth_token.key})
            return Response({"error": "Account not verified"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
