from django.db import models
from store.models import Seller

class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    
    name = models.CharField(max_length = 100, blank = False)
    description = models.TextField(max_length = 1000, blank = False)
    photo = models.ImageField(upload_to="product", blank = False)
    amount = models.IntegerField(blank = False)
    price = models.FloatField(blank = False)
    seles = models.IntegerField(default = 0)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
class ImagesProduct(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    
    image = models.ImageField(upload_to="product/images")
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)