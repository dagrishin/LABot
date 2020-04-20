from django.urls import path

from tickets.views import Words

urlpatterns = [
    path('words/', Words.as_view()),
]