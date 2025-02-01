from django.contrib import admin
from .models import Catalog


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ("name", "short_desc", "slug", "created_at", "updated_at")
    search_fields = ("name", "desc")
    list_filter = ("created_at", "updated_at")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name", "-created_at")
    fields = ("name", "desc", "slug", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")

    def short_desc(self, obj):
        return obj.desc[:50] + "..." if obj.desc and len(obj.desc) > 50 else obj.desc
    short_desc.short_description = "Description"