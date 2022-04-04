from dataclasses import field, fields
from re import search
from django.contrib import admin
from . import models
from django.utils.html import mark_safe


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class RoomTypeAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()

    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    fieldsets = (
        ("Basic Info", {"fields": ("name", "description", "country", "city", "price")}),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedroom", "baths")}),
        (
            "More About Spaces",
            {"classes": ("collapse",), "fields": ("amenity", "facility", "house_rule")},
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedroom",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "city",
        "country",
    )

    raw_id_fields = ("host",)

    search_fields = ("^city", "^host__username")

    filter_horizontal = ("amenity", "facility", "house_rule")

    def count_amenities(self, obj):
        return obj.amenity.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width=50px src="{obj.file.url}"/>')

    get_thumbnail.short_description = "THUMBNAIL"
