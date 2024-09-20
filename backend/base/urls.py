from django.urls import path
from . import views

urlpatterns=[
    
    path("items_list/", views.ListCreateItemsView.as_view()),
    path("add_item/", views.CreateItemView.as_view()),
    path("get_item/<int:pk>", views.GetItemView.as_view()),
    path("update_item/<int:pk>", views.UpdateItemView.as_view()),
    path("delete_item/<int:pk>", views.DeleteItemView.as_view()),
    path("add_tag/", views.ListCreateTagView.as_view()),
    path("tags_list/", views.ListCreateTagView.as_view()),
    path("update_tag/<int:pk>", views.UpdateTagView.as_view()),
    path("delete_tag/<int:pk>", views.DeleteTagView.as_view())
]