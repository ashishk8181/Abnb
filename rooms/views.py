from urllib import request
from xml.parsers.expat import model
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django_countries import countries
from . import models, forms


class HomeView(ListView):

    """Home View Definition"""

    model = models.Room
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"


class room_detail(DetailView):
    """Detail View Definition"""

    model = models.Room


def search(request):

    country = request.GET.get("country")

    if country:
        form = forms.SearchForm(request.GET)

        if form.is_valid():
            # print(form.cleaned_data)
            city = form.cleaned_data.get("city")
            country = form.cleaned_data.get("country")
            price = form.cleaned_data.get("price")
            room_type = form.cleaned_data.get("room_type")
            guests = form.cleaned_data.get("guests")
            bedroom = form.cleaned_data.get("bedroom")
            beds = form.cleaned_data.get("beds")
            baths = form.cleaned_data.get("baths")
            instant_book = form.cleaned_data.get("instant_book")
            superhost = form.cleaned_data.get("superhost")
            amenities = form.cleaned_data.get("amenities")
            facilities = form.cleaned_data.get("facilities")

            filter_args = {}

            if city != "Anywhere":
                filter_args["city_startswith"] = city

            filter_args["country"] = country

            if room_type is not None:
                filter_args["room_type"] = room_type

            if price is not None:
                filter_args["price__lte"] = price

            if guests is not None:
                filter_args["guests__gte"] = guests

            if bedroom is not None:
                filter_args["bedroom__gte"] = bedroom

            if beds is not None:
                filter_args["beds__gte"] = beds

            if baths is not None:
                filter_args["baths__gte"] = baths

            if instant_book:
                filter_args["instant_book"] = True

            if superhost:
                filter_args["host__superhost"] = True

            for amenity in amenities:
                filter_args["amenity"] = amenity

            for facility in facilities:
                filter_args["facility"] = facility

            qs = models.Room.objects.filter(**filter_args).order_by("-created")

            paginator = Paginator(qs, 10, orphans=5)

            page = request.GET.get("page", 1)

            rooms = paginator.get_page(page)

            return render(request, "rooms/search.html", {"form": form})

    else:
        form = forms.SearchForm()

    return render(request, "rooms/search.html", {"form": form})
