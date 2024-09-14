from django.db import models
from django.utils import timezone


class modelTag(models.Model):
    type = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    prefix = models.CharField(max_length=20)

    def __str__(self):
        return self.model_name