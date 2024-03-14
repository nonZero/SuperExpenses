import json
import random

from django.core.management.base import BaseCommand
from faker import Faker

from expenses.models import Expense, Category

import tqdm


class Command(BaseCommand):
    help = "Creates fake expenses."

    def add_arguments(self, parser):
        parser.add_argument("n", type=int)

    def handle(self, n, *args, **options):
        faker = Faker()

        Category.objects.all().delete()
        Expense.objects.all().delete()

        categories = [Category.objects.create(name=faker.sentence()) for i in range(8)]
        for i in tqdm.tqdm(range(n)):
            o = Expense(
                category=random.choice(categories),
                title=faker.sentence(),
                amount=round(random.randint(1000, 9999) / 10, 2),
                date=faker.date_this_year(),
                description="\n".join(faker.paragraph() for i in range(3)),
                more_data=json.loads(faker.json()),
            )
            o.save()
