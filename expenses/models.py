from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="expenses", )
    title = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)
    more_data = models.JSONField()

    def __str__(self):
        return f"{self.title} ${self.amount}"
