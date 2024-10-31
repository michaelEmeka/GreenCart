from django.shortcuts import render
from rest_framework import status
from rest_framework import serializers
from rest_framework.generics import ListAPIView, ListCreateAPIView, GenericAPIView, DestroyAPIView, UpdateAPIView
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
class ListCreateItemsView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Item.objects.all()
    serializer_class = ListItemSerializer

class CreateItemView(GenericAPIView):
    serializer_class = CreateItemSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
class GetItemView(GenericAPIView):
    serializer_class = GetItemSerializer
    queryset = Item.objects.all()

    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        if not Item.objects.filter(id=pk).exists():
            return Response({"message": "object does not exist"}, status=status.HTTP_204_NO_CONTENT)
        item = Item.objects.get(id=pk)
        serializer = self.serializer_class(item)
        #serializer.is_valid()
        return Response(serializer.data)
        
class UpdateItemView(GenericAPIView):
    '''
    Update Item Details
    '''
    serializer_class = UpdateItemSerializer
    queryset = Item.objects.all()
    
    def patch(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        if not Item.objects.filter(id=pk).exists():
            return Response({"message": "object does not exist"}, status=status.HTTP_204_NO_CONTENT)
        item = Item.objects.get(id=pk)
        serializer = self.serializer_class(item,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DeleteItemView(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = DeleteItemSerializer

class ListCreateTagView(ListCreateAPIView):
    queryset = ItemTag.objects.all()
    serializer_class = BaseTagSerializer

class UpdateTagView(UpdateAPIView):
    queryset = ItemTag.objects.all()
    serializer_class = BaseTagSerializer
    
class DeleteTagView(DestroyAPIView):
    queryset = ItemTag.objects.all()
    serializer_class = BaseTagSerializer