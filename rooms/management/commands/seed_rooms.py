import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users.models import User as user


class Command(BaseCommand):

    help = "This command creates many rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many rooms do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedroom": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        house_rule = room_models.HouseRule.objects.all()

        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(5, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1,31)}.webp",
                )
            for a in amenities:
                if random.randint(1, 15) % 2 == 0:
                    room.amenity.add(a)
            for f in facilities:
                if random.randint(1, 15) % 2 == 0:
                    room.facility.add(f)
            for h in house_rule:
                if random.randint(1, 15) % 2 == 0:
                    room.house_rule.add(h)
        self.stdout.write(self.style.SUCCESS(f"{number } Rooms created!"))
