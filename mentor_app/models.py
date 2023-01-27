from django.db import models
from django.contrib.auth.models import AbstractUser
from django_enum import EnumField
from . import enums


class User(AbstractUser):
    grade = EnumField(enums.GradeEnum, null=True, default=None)

    def __str__(self):
        return self.username
