import json
import bcrypt

from rest_framework            import viewsets, permissions
from rest_framework.decorators import api_view, action
from rest_framework.response   import Response

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Count

from .models      import House, DoorUseLog
from .serializers import HouseSerializer, HouseDetailSerializer, DoorUserLogSerializer
from .permissions import IsAdminOrOwner

HOUSE_ADMIN_TEST = "0000"
UNIT_COST = 1

# 관리자 전체 세대 리스트
class CostAdminViewSet(viewsets.ReadOnlyModelViewSet):
    queryset           = House.objects.annotate(cost=Count('dooruselog') * UNIT_COST)
    serializer_class   = HouseSerializer
    permission_classes = [permissions.IsAdminUser]

#  상세 관리비
class CostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset           = House.objects.annotate(cost=Count('dooruselog') * UNIT_COST)
    serializer_class   = HouseDetailSerializer
    permission_classes = [IsAdminOrOwner]

    @action(detail=True)
    def cost(self, request, *args, **kwargs):
        house = self.get_object()
        return Response(house.cost)

# 전체 로그
class DoorUseLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset           = DoorUseLog.objects.all()
    serializer_class   = DoorUserLogSerializer
    permission_classes = [permissions.IsAdminUser]