from email.policy import default
from typing_extensions import Required
from django import forms
from django_countries.fields import CountryField
from pkg_resources import require
from . import models


class SearchForm(forms.Form):

    city = forms.CharField(initial="Anywhere")
    country = CountryField(default="IN").formfield()
    price = forms.IntegerField(required=False)
    room_type = forms.ModelChoiceField(
        queryset=models.RoomType.objects.all(),
        empty_label="Any Kind",
        required=False,
    )
    guests = forms.IntegerField(required=False)
    bedroom = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    facilities = forms.ModelMultipleChoiceField(
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
