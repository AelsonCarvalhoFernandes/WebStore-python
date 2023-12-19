from django.contrib import admin
from .models import Product, ImagesProduct

@admin.register(Product)
class Product_Admin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'seller', 'amount', 'seles', 'updated_at']
    search_fields = ['name', 'seller']
    list_filter = ['amount', 'seller', 'created_at', 'updated_at']
    list_per_page = 20

@admin.register(ImagesProduct)    
class ImagesProduct_Admin(admin.ModelAdmin):
    model = ImagesProduct
    list_display = ['product']
    list_per_page = 20
    list_filter = ['created_at', 'updated_at']
