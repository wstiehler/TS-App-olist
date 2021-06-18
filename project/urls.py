from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="base"),
    path("", include("register_car.urls")),
    path("admin/", admin.site.urls),
]
