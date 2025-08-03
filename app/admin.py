from django.contrib import admin

from app.models import TechCategory, Technology


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass


@admin.register(TechCategory)
class TechCategoryAdmin(admin.ModelAdmin):
    pass
