from django.core.validators import MinLengthValidator
from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=10, validators=[MinLengthValidator(5)], unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

        def __str__(self):
            return self.name
