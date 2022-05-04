import imp
from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path("<int:pk>", views.room_detail.as_view(), name="detail"),
    path("search/", views.search, name="search"),
]
