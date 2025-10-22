from django.db import models
from django.utils.text import slugify

from helpers.base_model import BaseModel


class TechCategory(BaseModel):
    """
    A model that store information about a tech stack category e.g
    Frontend, Backend, Database etc.
    """

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Tech Categories"

    def __str__(self):
        return self.name


class Technology(BaseModel):
    """
    A model that store information about a tech stack e.g
    HTML, CSS, JavaScript, Django etc.
    """

    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        TechCategory,
        on_delete=models.CASCADE,
        related_name="technologies",
    )

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name


class Service(BaseModel):
    """
    A model for listing all the Services that I offer.
    """

    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True, default="")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title


class Testimonial(BaseModel):
    """
    A model for listing all the Testimonials.
    """

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(
        upload_to="uploads/testimonials/photos/",
        blank=True,
        null=True,
    )
    quote = models.TextField()

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.name} ({self.role})"

    def short_message(self):
        """Return a shortened version of the testimonial message."""
        return self.quote[:75] + ("..." if len(self.quote) > 75 else "")


class Project(BaseModel):
    """
    A model for listing all the Projects.
    """

    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True, max_length=100)
    short_form = models.CharField(max_length=11, blank=True, default="")
    description = models.TextField()
    link = models.URLField(blank=True, default="")
    image = models.ImageField(
        upload_to="uploads/projects/screenshots/",
        blank=True,
        default="default.jpg",
    )
    technologies = models.TextField(blank=True, default="")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        if self.short_form:
            return f"{self.title} ({self.short_form})"
        return self.title
