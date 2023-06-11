
from django.db import models
from django.urls import reverse

from users.models import User


class Users(models.Model):
    title = models.CharField(max_length=225)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=50)
    cabinet = models.CharField(max_length=50)
    gender = models.ForeignKey('Gender', on_delete=models.PROTECT, verbose_name='Гендер', null=True)
    phone = models.CharField(max_length=150)
    speciality = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Специализация', null=True)
    about = models.CharField(max_length=1000)
    age = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='image/about/', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Специалисты'
        verbose_name_plural = 'Специалисты'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, null=True)

    def __str__(self):
        return self.name


class Gender(models.Model):
    pol = models.CharField(max_length=100, db_index=True, null=True)

    def __str__(self):
        return self.pol


class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='image/products')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'Анализ: {self.name} | Категория: {self.category.name}'


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

