# Generated by Django 5.0.3 on 2024-03-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0003_category_expense_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="more_data",
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
    ]
