from django.db import models
from shop.models import Product
from django.contrib.auth.models import User


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    active = models.BooleanField(default=True)

    def subtotal(self):
        return self.quantity * self.products.price

    def __str__(self):
        return self.products.name


class Account(models.Model):
    accnumber = models.CharField(max_length=200)
    acctype = models.CharField(max_length=200)
    amount = models.IntegerField()

    def __str__(self):
        return self.accnumber


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(max_length=100)
    order_status = models.CharField(max_length=200, default="Pending")
    delivery_status = models.CharField(max_length=200, default="Pending")
    noofitems = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
