from django.db import models
from django.db.models.deletion import CASCADE
from shopapp.models import product
# Create your models here.

class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date=models.DateField(auto_now_add=True)
    class Meta:
        db_table='Cart'
        ordering=['date']
    def __str__(self):
            return '{}'.format(self.cart_id)

class Cart_item(models.Model):
    Product=models.ForeignKey(product,on_delete=models.CASCADE)
    Cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='Cartitem'
    
    def sub_total(self):
        return self.Product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.Product) 
