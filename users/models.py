import random

from django.contrib.auth.models import AbstractUser
from django.db import models


def random_number():
    return random.randint(1, 100)


class CustomUser(AbstractUser):
    birthday = models.DateField(null=True)
    number = models.IntegerField(default=random_number)
