import random
from secrets import choice
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_models
from users import models as users_models
from rooms import models as rooms_models


class Command(BaseCommand):

    help = "This command creates many lists"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many lists do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = users_models.User.objects.all()
        rooms = rooms_models.Room.objects.all()
        seeder.add_entity(
            list_models.List,
            number,
            {
                "user": lambda x: random.choice(users),
                # "room": lambda x: random.choice(rooms),
            },
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(5, 30)]
            list_model.room.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f"{number} Lists created!"))
