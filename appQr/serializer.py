from rest_framework import serializers
from .models import ZonaRiego

class ZonaRiegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZonaRiego
        fields = '__all__'
