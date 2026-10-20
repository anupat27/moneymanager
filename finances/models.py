from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('EXPENSE', 'Expense'),
        ('INCOME', 'Income'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    category = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user} - {self.transaction_type} - {self.amount:.2f}"

