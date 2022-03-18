from unicodedata import name
from django.db import models
from core import models as core_models


class List(core_models.TimeStamped):

    """List Model Definition"""

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooom = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name
