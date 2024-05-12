from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_change = models.IntegerField()  # Positive for addition, negative for deduction
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} - {self.quantity_change}"

