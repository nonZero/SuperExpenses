from django.urls import path

from expenses.views import expense_list

app_name = "expenses"

urlpatterns = [
    path("", expense_list),
]
