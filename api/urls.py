from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'admin', views.CostAdminViewSet, basename="admin")
router.register(r'v1/public', views.CostViewSet)
router.register(r'door-use-log', views.DoorUseLogViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
