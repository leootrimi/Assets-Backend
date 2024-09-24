from django.db import models

class EquipmentRequest(models.Model):

    full_name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=50)
    department = models.CharField(max_length=255)
    contact_info = models.EmailField(max_length=255)
    equipment_type = models.CharField(max_length=255)
    urgency = models.CharField(max_length=10)
    justification = models.TextField()
    status = models.CharField(max_length=10, default='Pending')

    def __str__(self):
        return f"{self.full_name} - {self.equipment_type}"