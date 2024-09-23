from typing import TYPE_CHECKING

from django.contrib.auth.decorators import login_required

from cars.models import Car

if TYPE_CHECKING:
    from django.http import HttpResponse, HttpRequest


def login(request: "HttpRequest") -> "HttpResponse":
    pass


def registration(request: "HttpRequest") -> "HttpResponse":
    pass


@login_required
def profile(request: "HttpRequest") -> "HttpResponse":
    pass


@login_required
def logout(request: "HttpRequest") -> "HttpResponse":
    pass
