from django.urls import path
from . import views

urlpatterns=[
    
    path("items_list/", views.ListCreateItemsView.as_view()),
    path("add_item/", views.CreateItemView.as_view()),
    path("get_item/<int:pk>", views.GetItemView.as_view())
]