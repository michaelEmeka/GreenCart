from django.db import models
from users.models import User
from base.models import Item

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
