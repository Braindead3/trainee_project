from rest_framework import serializers
from .models import CarShowroom


class CarShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowroom
        fields = ['pk', 'name', 'country', 'preferred_characteristics', 'balance']
