from django.urls import path
from . import views
urlpatterns = [
    path("modify-cart-item/<int:pk>/", views.ModifyCartItem.as_view()),
    path("remove-cart-item/<int:pk>/", views.ModifyCartItem.as_view()),
    path("cart-items/", views.ListOpenCartItems.as_view())
    ]