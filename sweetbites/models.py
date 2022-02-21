from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=200)
    original_price = models.CharField(max_length=200)
    discount_price = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    description = models.CharField(max_length=200)
    
class orders(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    
class cart(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)