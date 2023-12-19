from django.db import models
from django.contrib.auth.models import AbstractUser

STATUS = (
    ("Ac", "Activate"),
    ("bl", "Blocked"),
    ("ba", 'Banned')
)

class User(AbstractUser):
    status = models.CharField(max_length = 2, choices = STATUS)
    photo = models.ImageField(upload_to='users')

    def __str__(self) -> str:
        return self.username
    
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    cpf = models.CharField(max_length = 16)
    cellphone = models.CharField(max_length = 12)
    state = models.CharField(max_length = 30)
    city = models.CharField(max_length = 50)
    street = models.CharField(max_length = 150)
    number = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.user.username

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length = 100)
    cnpj = models.CharField(max_length = 26)

    instagran = models.URLField()
    email = models.EmailField()
    cellphone = models.CharField(max_length = 15)

    state = models.CharField(max_length = 30)
    city = models.CharField(max_length = 50)
    street = models.CharField(max_length = 150)
    number = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.name
