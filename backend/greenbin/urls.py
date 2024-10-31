from django.urls import path
from . import views

urlpatterns = [
    path("bin/submit_trash/<int:pk>/", views.SubmitTrash.as_view()),
]