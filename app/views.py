from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from app.models import Project, Service, TechCategory, Testimonial


def index(request: HttpRequest) -> HttpResponse:
    tech_categories = TechCategory.objects.prefetch_related("technologies").order_by("id").filter(is_active=True)
    services = Service.objects.filter(is_active=True).order_by("id")
    testmonials = Testimonial.objects.filter(is_active=True).order_by("id")
    projects = Project.objects.filter(is_active=True).order_by("id")

    context = {
        "tech_categories": tech_categories,
        "services": services,
        "testmonials": testmonials,
        "projects": projects,
    }
    return render(request, "index.html", context)


def project_details(request: HttpRequest, slug: str) -> HttpResponse:
    """
    View for project details
    """
    project = get_object_or_404(Project, slug=slug, is_active=True)
    context = {"project": project}
    return render(request, "portfolio-details.html", context)
