import imp
from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path("create/", views.AddRoomView.as_view(), name="create"),
    path("<int:pk>", views.Room_Detail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EditRoomView.as_view(), name="edit"),
    path("<int:pk>/photos/", views.RoomPhotosView.as_view(), name="photos"),
    path("<int:pk>/photos/upload/", views.AddPhotoView.as_view(), name="add-photo"),
    path("<int:room_pk>/photos/<int:photo_pk>/delete/", views.delete_photo, name="delete-photos"),
    path("<int:room_pk>/photos/<int:photo_pk>/edit/", views.EditPhotoView.as_view(), name="edit-photo"),
    path("search/", views.search, name="search"),
]
