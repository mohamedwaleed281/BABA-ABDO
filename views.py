from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Branch, Sales, Inventory, Expense
from .serializers import BranchSerializer, SalesSerializer, InventorySerializer, ExpenseSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class RecommendationView(APIView):
    def get(self, request):
        # Dummy Recommendation Logic
        recommendations = [{"day": i, "predicted_revenue": 1000 + i * 10} for i in range(1, 8)]
        return Response(recommendations)
