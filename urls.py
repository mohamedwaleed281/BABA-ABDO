from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet, SalesViewSet, InventoryViewSet, ExpenseViewSet, RecommendationView

router = DefaultRouter()
router.register('branches', BranchViewSet)
router.register('sales', SalesViewSet)
router.register('inventory', InventoryViewSet)
router.register('expenses', ExpenseViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/recommendations/', RecommendationView.as_view(), name='recommendations'),
]
