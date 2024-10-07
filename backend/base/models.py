from django.db import models
from users.models import User
from django.apps import apps
from django.apps import apps #to prevent circularr import


class ItemTag(models.Model):
    tag_name = models.CharField(max_length=50, blank=False, unique=True)
    
    def __str__(self):
        return self.tag_name


class Item(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="items")
    item_name = models.CharField(max_length=50, blank=False)
    item_description = models.TextField(blank=True)
    item_price = models.IntegerField(blank=False)
    #image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    item_tags = models.ManyToManyField(ItemTag,  related_name="items")
    
    def __str__(self):
        return self.item_name