import json
import bcrypt

from rest_framework import viewsets, permissions

from django.views   import View
from django.http    import JsonResponse
from django.db.models import Count


# from .permissions import IsOwner
from .models      import House, DoorUseLog
from .serializers import HouseSerializer

HOUSE_ADMIN_TEST = "0000"
UNIT_COST = 1

class CostAdminViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = House.objects.annotate(cost=Count('dooruselog') * UNIT_COST)
    serializer_class = HouseSerializer
    permission_classes = [permissions.IsAuthenticated]
    # def post(self, request):
    #     try:
    #         data     = json.loads(request.body)
    #         number   = data['number']
    #         password = data['password']

    #         if not House.objects.filter(number=number).exists():
    #             return JsonResponse({'message' : 'INVALID_HOUSE_NUMBER'}, status = 401)

    #         house = House.objects.get(number=number)

    #         if not bcrypt.checkpw(password.encode('utf-8'), house.password.encode('utf-8')):
    #             return JsonResponse({'message': 'INVALID_PASSWORD'}, status=401)
            
    #         if number == HOUSE_ADMIN_TEST:
    #             costs = [
    #                 {
    #                     i.number : DoorUseLog.objects.filter(house_number__number=i.number).count() * UNIT_COST
    #                 } for i in House.objects.all()
    #             ]
    #             return JsonResponse({"costs" : costs}, status=200)

    #         cost = DoorUseLog.objects.filter(house_number__number=number).count() * UNIT_COST
    #         return JsonResponse({"cost" : cost}, status=200)

    #     except KeyError:
    #         return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        