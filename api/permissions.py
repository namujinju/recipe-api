from rest_framework import permissions

HOUSE_ADMIN_TEST = "0000"
UNIT_COST = 1

class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user) | (request.user.is_staff)
