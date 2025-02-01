from django.db import models
from django.utils.text import slugify
from authors.base_model import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name="Tag Name")
    slug = models.SlugField(unique=True, blank=True, verbose_name="URL Slug")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Django slugify ishlatish
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}" # Agar '#' belgisini xohlasangiz, f"#{self.name}" qoldiring

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
