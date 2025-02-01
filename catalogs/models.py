from django.db import models
from authors.base_model import BaseModel
from django.utils.text import slugify


class Catalog(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name="Catalog Name", db_index=True)
    desc = models.TextField(blank=True, null=True, default="", verbose_name="Description")
    slug = models.SlugField(unique=True, blank=True, verbose_name="URL Slug")

    def get_unique_slug(self):
        """Slug yaratishda takrorlanish oldini oladi."""
        base_slug = slugify(self.name)
        slug = base_slug
        count = 1
        while Catalog.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{count}"
            count += 1
        return slug

    def save(self, *args, **kwargs):
        """Slugni avtomatik yaratish va takrorlanishini oldini olish."""
        if not self.slug:
            self.slug = self.get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        """Admin panelda va boshqa joylarda to‘g‘ri ko‘rinish uchun."""
        return self.name

    class Meta:
        verbose_name = "Catalog"
        verbose_name_plural = "Catalogs"
