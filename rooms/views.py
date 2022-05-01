from xml.parsers.expat import model
from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):

    """Home View Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"


class room_detail(DetailView):
    """Detail View Definition"""

    model = models.Room
