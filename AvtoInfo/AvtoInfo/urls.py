from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("cars.urls")),
    path("user/", include("users.urls")),
    path("admin/", admin.site.urls),
]
