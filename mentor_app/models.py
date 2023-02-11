from django.db import models
from django.contrib.auth.models import AbstractUser
from django_enum import EnumField


class GradeEnum(models.TextChoices):
    JUNIOR = 'Junior'
    JUNIOR_PLUS = 'Junior+'
    MIDDLE = 'Middle'
    MIDDLE_PLUS = 'Middle+'
    SENIOR = 'Senior'


class User(AbstractUser):
    grade = EnumField(GradeEnum, null=True, default=None)

    def __str__(self):
        return self.username


class Area(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=100)
    grade = EnumField(GradeEnum, null=True, default=None)

    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
