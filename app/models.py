from django.db import models

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
