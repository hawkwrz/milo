import random

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    birthday = models.DateField(null=True)
    number = models.IntegerField(default=random.randint(1, 100))
