import random

from django.core.management.base import BaseCommand
from faker import Faker

from expenses.models import Expense

import tqdm


class Command(BaseCommand):
    help = "Creates fake expenses."

    def add_arguments(self, parser):
        parser.add_argument("n", type=int)

    def handle(self, n, *args, **options):
        faker = Faker()
        for i in tqdm.tqdm(range(n)):
            o = Expense(
                title=faker.sentence(),
                amount=round(random.randint(1000, 9999) / 10, 2),
                date=faker.date_this_year(),
            )
            o.save()
