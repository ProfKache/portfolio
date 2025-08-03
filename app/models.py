from django.db import models


class TechCategory(models.Model):
    """
    A model that store information about a tech stack category e.g
    Frontend, Backend, Database etc.
    """

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Tech Categories"

    def __str__(self):
        return self.name


class Technology(models.Model):
    """
    A model that store information about a tech stack e.g
    HTML, CSS, JavaScript, Django etc.
    """

    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(TechCategory, on_delete=models.CASCADE, related_name="technologies")

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name
