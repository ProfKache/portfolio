from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from app.models import TechCategory


def index(request: HttpRequest) -> HttpResponse:
    tech_categories = TechCategory.objects.prefetch_related("technologies").order_by("id").all()

    context = {"tech_categories": tech_categories}
    return render(request, "index.html", context)
