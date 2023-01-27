from django.db import models


class GradeEnum(models.TextChoices):
    JUNIOR = 'Junior'
    JUNIOR_PLUS = 'Junior+'
    MIDDLE = 'Middle'
    MIDDLE_PLUS = 'Middle+'
    SENIOR = 'Senior'
