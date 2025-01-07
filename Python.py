 restaurant_management/
├── manage.py
├── restaurant_management/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   ├── celery.py
├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── signals.py
│   ├── tasks.py
│   ├── recommendations.py

INSTALLED_APPS = [
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    'django_celery_beat',
    'api',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'restaurant_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'




from django.db import models
from django.contrib.auth.models import AbstractUser

class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

class Sales(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='sales')
    total_orders = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[('Cash', 'Cash'), ('Card', 'Card'), ('App', 'App')])
    date = models.DateField(auto_now_add=True)

class Inventory(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='inventory')
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    threshold = models.IntegerField()

class Expense(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='expenses')
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)



from rest_framework import serializers
from .models import Branch, Sales, Inventory, Expense

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'



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


from celery import shared_task

@shared_task
def send_notification_email():
    # Logic to send notification email
    return "Email Sent"




