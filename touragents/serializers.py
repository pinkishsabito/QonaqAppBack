from rest_framework import serializers
from .models import TourAgent


class TourAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourAgent
        fields = '__all__'
