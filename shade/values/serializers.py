from rest_framework import serializers
from .models import ShadeVariation


class ShadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShadeVariation
        fields = '__all__'
        