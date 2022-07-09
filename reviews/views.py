from django.shortcuts import redirect, reverse
from django.contrib import messages
from . import forms
from rooms import models as room_models

def create_review(requset, room):
    if requset.method == "POST":
        form =forms.CreateReviewForm(requset.POST)
        room = room_models.Room.objects.get_or_none(pk=room)
        if not room:
            return redirect(reverse("core:home"))
        if form.is_valid():
            review = form.save()
            review.room = room
            review.user = requset.user
            review.save()
            messages.success(requset, "Review Published")
            return redirect(reverse("room:detail", kwargs={"pk":room.pk}))
        
        else:
            return redirect(reverse("core:home"))
