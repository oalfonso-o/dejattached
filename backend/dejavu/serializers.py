from rest_framework import serializers
from dejavu.models import Day


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'name', 'weekday')
        read_only_fields = ('name', 'weekday')
