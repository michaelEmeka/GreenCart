from django.db import models
#from users.models import User

class ItemTag(models.Model):
    tag_name = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.tag_name


class Item(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50, blank=False)
    item_description = models.TextField(blank=True)
    item_price = models.IntegerField(blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)
    item_tags = models.ManyToManyField(ItemTag,  related_name="items")
    
    def __str__(self):
        return self.item_name

