from rest_framework import serializers
from .models import EquipmentRequest

class ESerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentRequest
        fields = '__all__'