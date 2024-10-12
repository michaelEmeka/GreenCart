from django.db import models
from users.models import User
from base.models import Item
import uuid

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    is_closed = models.BooleanField(default=False)

    def get_cart_total(self):
        total = 0
        for cart_item in self.cart_items.all():
            total += cart_item.get_cartitem_total
        return total

    def __str__(self):
        return self.user.business_name + "'s cart " + str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def get_cartitem_total(self):
        return self.item.item_price * self.quantity

    def __str__(self):
        return self.cart.user.business_name + "\'s " + self.item.item_name

class Checkout(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="orders")
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    is_success = models.BooleanField(default=False)
    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.address
