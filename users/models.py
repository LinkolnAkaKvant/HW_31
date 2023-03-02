from django.contrib.auth.models import AbstractUser
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.name


class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Администратор'
        MODERATOR = 'moderator', 'Модератор'
        MEMBER = 'member', 'Пользователь'

    role = models.CharField(max_length=50, choices=Roles.choices, default=Roles.MEMBER)
    age = models.PositiveIntegerField(null=True)
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
