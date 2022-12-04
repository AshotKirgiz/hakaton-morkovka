from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

class NewBid(models.Model):
    pass

class CustomUser(AbstractUser):
    fio = models.TextField('ФИО', blank=True, )
    job = models.TextField('Место работы и должность', blank=True,)
    theme = models.TextField('Тема и аннотациия', blank=True,)
    media = models.TextField('Ссылка на материал', blank=True,)