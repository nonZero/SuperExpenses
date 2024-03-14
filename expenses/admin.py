from django.contrib import admin

from expenses.models import Expense, Category


class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'amount',
        'date',
        'id',
        'category',
    )
    search_fields = (
        'title',
        'amount',
        'date',
        'id',
    )
    date_hierarchy = 'date'


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category)
