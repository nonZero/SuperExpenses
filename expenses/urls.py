from django.urls import path

from expenses.views import ExpenseListView, ExpenseDetailView

app_name = "expenses"

urlpatterns = [
    path("", ExpenseListView.as_view()),
    path("<int:pk>/", ExpenseDetailView.as_view()),
]
