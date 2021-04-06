from rest_framework import serializers

from .models import House, DoorUseLog

class HouseSerializer(serializers.ModelSerializer):
    cost = serializers.IntegerField()

    class Meta:
        model  = House
        fields = ['url', 'cost', 'number']

class HouseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model  = House
        fields = ['url', 'number']

class DoorUserLogSerializer(serializers.ModelSerializer):
    house_number = serializers.SerializerMethodField()

    def get_house_number(self, obj):
        return obj.house_number.number

    class Meta:
        model  = DoorUseLog
        fields = ['id', 'created_at', 'house_number']