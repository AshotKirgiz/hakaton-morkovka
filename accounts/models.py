from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import *
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
    scores = models.DecimalField('Баллы', max_digits=5, decimal_places=2, blank=False, default=0)

class CustomScore(models.Model):
    score1 = models.IntegerField('Оценка1', null=True, validators=
    [MaxValueValidator(limit_value=10), MinValueValidator(limit_value=0)]
                                 )
    score2 = models.IntegerField('Оценка2', null=True, validators=
    [MaxValueValidator(limit_value=15), MinValueValidator(limit_value=0)]
                                 )
    score3 = models.IntegerField('Оценка3', null=True, validators=
    [MaxValueValidator(limit_value=10), MinValueValidator(limit_value=0)]
                                 )
    score4 = models.IntegerField('Оценка4', null=True, validators=
    [MaxValueValidator(limit_value=15), MinValueValidator(limit_value=0)]
                                 )
    score5 = models.IntegerField('Оценка5', null=True, validators=
    [MaxValueValidator(limit_value=10), MinValueValidator(limit_value=0)]
                                 )
    score6 = models.IntegerField('Оценка6', null=True, validators=
    [MaxValueValidator(limit_value=10), MinValueValidator(limit_value=0)]
                                 )
    score7 = models.IntegerField('Оценка7', null=True, validators=
    [MaxValueValidator(limit_value=15), MinValueValidator(limit_value=0)]
                                 )
    score8 = models.IntegerField('Оценка8', null=True, validators=
    [MaxValueValidator(limit_value=15), MinValueValidator(limit_value=0)]
                                 )
    score9 = models.IntegerField('Оценка9', null=True, validators=
    [MaxValueValidator(limit_value=20), MinValueValidator(limit_value=0)]
                                 )
    score10 = models.IntegerField('Оценка10', null=True, validators=
    [MaxValueValidator(limit_value=30), MinValueValidator(limit_value=0)]
                                 )
    score11 = models.IntegerField('Оценка11', null=True, validators=
    [MaxValueValidator(limit_value=20), MinValueValidator(limit_value=0)]
                                 )
    score12 = models.IntegerField('Оценка12', null=True, validators=
    [MaxValueValidator(limit_value=5), MinValueValidator(limit_value=0)]
                                 )
    score13 = models.IntegerField('Оценка13', null=True, validators=
    [MaxValueValidator(limit_value=5), MinValueValidator(limit_value=0)]
                                 )
    score14 = models.IntegerField('Оценка14', null=True, validators=
    [MaxValueValidator(limit_value=8), MinValueValidator(limit_value=0)]
                                 )
    score15 = models.IntegerField('Оценка15', null=True, validators=
    [MaxValueValidator(limit_value=12), MinValueValidator(limit_value=0)]
                                 )
    score16 = models.IntegerField('Оценка16', null=True, validators=
    [MaxValueValidator(limit_value=10), MinValueValidator(limit_value=0)]
                                 )
    score17 = models.IntegerField('Оценка17', null=True, validators=
    [MaxValueValidator(limit_value=10), MinValueValidator(limit_value=0)]
                                 )

