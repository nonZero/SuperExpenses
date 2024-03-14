from django.shortcuts import render
from django.views.generic import ListView, DetailView

from expenses.models import Expense


class ExpenseListView(ListView):
    model = Expense
    ordering = "-date"


class ExpenseDetailView(DetailView):
    model = Expense



