from rest_framework import serializers

from .models import House, DoorUseLog

class HouseSerializer(serializers.HyperlinkedModelSerializer):
    cost = serializers.IntegerField()

    class Meta:
        model  = House
        fields = ['url', 'cost', 'number']