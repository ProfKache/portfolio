from django.contrib import admin

from app.models import Service, TechCategory, Technology, Testimonial


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass


@admin.register(TechCategory)
class TechCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "is_active", "created_at", "updated_at")
    list_filter = ("is_active",)
    list_editable = ("is_active",)
    search_fields = ("name", "role", "message")
