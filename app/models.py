from django.db import models


class Technology(models.Model):
    """
    A model that store information about a tech stack e.g
    HTML, CSS, JavaScript, Django etc.
    """

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name
