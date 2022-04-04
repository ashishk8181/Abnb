from asyncio.windows_events import NULL
from distutils.command.upload import upload
from locale import currency
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """Custom User Models"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_FRENCH = "fr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_FRENCH, "French"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_GBP = "gbp"
    CURRENCY_EUR = "eur"
    CURRENCY_INR = "inr"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_INR, "INR"),
        (CURRENCY_GBP, "GBP"),
        (CURRENCY_EUR, "EUR"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
