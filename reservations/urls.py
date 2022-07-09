from unicodedata import name
from . import views
from django.urls import path

app_name ="reservations"

urlpatterns = [
    path(
        "create/<int:room>/<int:year>-<int:month>-<int:day>",
        views.create,
        name="create"
    ),
    path("<int:pk>", views.Reservation_detail.as_view(), name="detail"),
    path("<int:pk>/<str:verb>", views.edit_reservation, name="edit"),

]
