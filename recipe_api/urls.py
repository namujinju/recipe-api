from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api import views
router = DefaultRouter()
router.register(r'api/admin', views.CostAdminViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
