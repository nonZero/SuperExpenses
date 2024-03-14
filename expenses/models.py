from django.db import models


class Expense(models.Model):
    title = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} ${self.amount}"
