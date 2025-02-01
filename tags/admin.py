from django.contrib import admin
from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name", "-created_at")
    fields = ("name", "slug", "created_at", "updated_at")  # `created_at` va `updated_at` qo‘shildi
    readonly_fields = ("created_at", "updated_at")  # `slug` readonly emas

    def save_model(self, request, obj, form, change):
        """Agar slug bo‘sh bo‘lsa, avtomatik generatsiya qilish"""
        if not obj.slug:
            from django.utils.text import slugify
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)
