from django.db import models
from django.utils import timezone


class Equipment(models.Model):
    employer = models.ForeignKey('employers.Employers', on_delete=models.SET_NULL, related_name='equipments', null=True)
    role = models.CharField(max_length=100)
    purchase_date = models.DateField(default=timezone.now)
    date_of_receipt = models.DateField(default=timezone.now)
    warranty_expiration_date = models.DateField(null=True, blank=True)
    supplier = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    serial_no = models.CharField(max_length=100)
    tag = models.CharField(max_length=100, blank=True, null=True)
    assigned_form = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    departament = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.equipment_type} - {self.model} ({self.serial_no})"
