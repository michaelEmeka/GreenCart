from django.urls import path
from . import views
urlpatterns = [
    path("add-to-cart/<int:pk>/", views.AddItemToCart.as_view()),
    ]