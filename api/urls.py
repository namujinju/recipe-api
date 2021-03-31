from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views      import CostAdminViewSet

router = DefaultRouter()
router.register(r'admin', CostAdminViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
]
