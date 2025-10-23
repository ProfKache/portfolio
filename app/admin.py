from django.contrib import admin

from app.models import Project, Service, TechCategory, Technology, Testimonial


class BaseModelAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "created_by", "updated_at", "updated_by")

    def save_model(self, request, obj, form, change):
        if not change:  # If creating new object
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        # Remove tracking fields from the form
        if obj is None:  # When creating new object
            return [
                f
                for f in fields
                if f
                not in (
                    "created_at",
                    "created_by",
                    "updated_at",
                    "updated_by",
                )
            ]
        return fields


@admin.register(Technology)
class TechnologyAdmin(BaseModelAdmin):
    list_display = (
        "name",
        "category__name",
        "created_at",
        "updated_at",
        "is_active",
    )
    list_filter = ("is_active",)
    list_editable = ("is_active",)


@admin.register(TechCategory)
class TechCategoryAdmin(BaseModelAdmin):
    list_display = ("name", "created_at", "updated_at", "is_active")
    list_filter = ("is_active",)
    list_editable = ("is_active",)


@admin.register(Service)
class ServiceAdmin(BaseModelAdmin):
    list_display = (
        "title",
        "description",
        "created_at",
        "updated_at",
        "is_active",
    )
    list_filter = ("is_active",)
    list_editable = ("is_active",)


@admin.register(Testimonial)
class TestimonialAdmin(BaseModelAdmin):
    list_display = (
        "name",
        "role",
        "created_at",
        "updated_at",
        "is_active",
    )
    list_filter = ("is_active",)
    list_editable = ("is_active",)
    search_fields = ("name", "role", "quote")


@admin.register(Project)
class ProjectAdmin(BaseModelAdmin):
    list_display = ("title", "is_active")
    list_editable = ("is_active",)
    prepopulated_fields = {"slug": ("title",)}
