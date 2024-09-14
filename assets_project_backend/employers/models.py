from django.db import models
from django.utils import timezone

class Employers(models.Model):
    name = models.CharField(max_length=100)
    personal_no = models.CharField(max_length=20)
    surname = models.CharField(max_length=100)
    birthday = models.DateField()
    position = models.CharField(max_length=20)
    # Contact Information
    phone_number_1 = models.CharField(max_length=15)
    address_1 = models.CharField(max_length=255)
    postal_code_1 = models.CharField(max_length=10)
    phone_number_2 = models.CharField(max_length=15, blank=True, null=True)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=20, null=True)
    reg_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} {self.surname}"




