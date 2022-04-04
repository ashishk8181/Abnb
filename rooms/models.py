from pydoc import describe
from unicodedata import name
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStamped):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """RoomType Model Definition"""

    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]


class Amenity(AbstractItem):

    """Amentiy Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """House_rule Model Definition"""

    class Meta:
        verbose_name = "House Rule"


class Room(core_models.TimeStamped):

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedroom = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenity = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facility = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rule = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        total_avg = 0
        for review in all_reviews:
            total_avg += review.rating_average()
        return total_avg / len(all_reviews)


class Photo(core_models.TimeStamped):

    """Photo Model Definition"""

    caption = models.CharField(max_length=100)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
