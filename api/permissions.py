from rest_framework import permissions

HOUSE_ADMIN_TEST = "0000"
UNIT_COST = 1

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if not House.objects.filter(number=number).exists():
            return JsonResponse({'message' : 'INVALID_HOUSE_NUMBER'}, status = 401)

        house = House.objects.get(number=number)

        if not bcrypt.checkpw(password.encode('utf-8'), house.password.encode('utf-8')):
            return JsonResponse({'message': 'INVALID_PASSWORD'}, status=401)
        
        return True
