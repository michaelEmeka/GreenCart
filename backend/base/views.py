from django.shortcuts import render
from rest_framework import status
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Item, ItemTag
from .serializers import *

#List Items
#Add Item
#Update Item
#Delete Item
#List Tags
#Add Tag
#Update Tag
#Delete Tag
class ListCreateItemsView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Item.objects.all()
    serializer_class = ListCreateItemSerializer

class CreateItemView(GenericAPIView):
    def post(self, request):
        serializer = CreateItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
class AddItemView(GenericAPIView):
    def post(self, request):
        serializer_class = AddItemSerializer
        #item_name, item_price, date_added,  item_tags
        
class GetItemView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        if not Item.objects.filter(id=pk).exists():
            return Response({"message": "object does not exist"}, status=status.HTTP_204_NO_CONTENT)
        item = Item.objects.get(id=pk)
        serializer = GetItemSerializer(item)
        #serializer.is_valid()
        return Response(serializer.data)
        
class UpdateItemView(GenericAPIView):
    '''
    Update Item Details
    '''
    def post(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        if not Item.objects.filter(id=pk).exists():
            return Response({"message": "object does not exist"}, status=status.HTTP_204_NO_CONTENT)
        item = Item.objects.get(id=pk)
        serializer = UpdateItemSerializer(item,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        if not Item.objects.filter(id=pk).exists():
            return Response({"message": "object does not exist"}, status=status.HTTP_204_NO_CONTENT)
        item = Item.objects.get(id=pk)
        serializer = GetItemSerializer(item)
        #serializer.is_valid()
        return Response(serializer.data)