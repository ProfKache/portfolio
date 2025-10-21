from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from app.models import Service, TechCategory


def index(request: HttpRequest) -> HttpResponse:
    tech_categories = TechCategory.objects.prefetch_related("technologies").order_by("id").filter(is_active=True)
    services = Service.objects.filter(is_active=True).order_by("id")

    context = {"tech_categories": tech_categories, "services": services}
    return render(request, "index.html", context)
