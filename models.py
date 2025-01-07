from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

class Sales(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="sales")
    total_orders = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[("Cash", "Cash"), ("Card", "Card"), ("App", "App")])
    date = models.DateField(auto_now_add=True)
