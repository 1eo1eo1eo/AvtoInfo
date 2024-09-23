from typing import TYPE_CHECKING

from django.core.paginator import Paginator
from django.shortcuts import render

from cars.models import Car, Comment

if TYPE_CHECKING:
    from django.http import HttpResponse, HttpRequest


def cars(request: "HttpRequest") -> "HttpResponse":

    queryset = Car.objects.order_by("id")

    context: dict = {
        "title": "Cars - Home",
        "cars": queryset,
    }
    return render(request, "cars/cars.html", context)
