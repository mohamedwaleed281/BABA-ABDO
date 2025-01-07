from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet, SalesViewSet

router = DefaultRouter()
router.register('branches', BranchViewSet)
router.register('sales', SalesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
