from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Client, Seller

@admin.register(User)
class User_admin(UserAdmin):
    model = User
    fieldsets = []

@admin.register(Client)
class Client_admin(admin.ModelAdmin):
    model = Client
    list_display = ['user', 'cpf','created_at', 'updated_at']

@admin.register(Seller)
class Seller_admin(admin.ModelAdmin):
    model = Seller
    list_display = ['user', 'cnpj','created_at', 'updated_at']