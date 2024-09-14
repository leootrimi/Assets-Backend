from rest_framework import serializers
from .models import Employers

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employers
        fields = '__all__'
