import os

from django.urls import path

from tickets.views import WordView, WordDetail

app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path("words/", WordView.as_view()),
    path("words/<int:pk>/", WordDetail.as_view()),
]
