from rest_framework import serializers
from .models import modelTag

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = modelTag
        fields = '__all__'
