from django.db import models
from authors.base_model import BaseModel
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from datetime import date


class Author(BaseModel):
    first_name = models.CharField(max_length=50, verbose_name="First Name", unique=True)
    last_name = models.CharField(max_length=50, verbose_name="Last Name", unique=True)
    bio = models.TextField(blank=True, null=True, verbose_name="Biography")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Birth Date")
    slug = models.SlugField(unique=True, blank=True, verbose_name="URL Slug")
    profile_picture = models.ImageField(upload_to='authors/', blank=True, null=True, verbose_name="Profile Picture")
    is_active = models.BooleanField(default=False, db_index=True)

    def clean(self):
        """Validatsiya: Tug‘ilgan sanani kelajak sanasiga o‘rnatib bo‘lmaydi."""
        if self.birth_date and self.birth_date > date.today():
            raise ValidationError({"birth_date": "Birth date cannot be in the future."})

    def get_unique_slug(self):
        """Slug yaratishda takrorlanish oldini oladi."""
        base_slug = slugify(f"{self.first_name}-{self.last_name}")
        slug = base_slug
        count = 1
        while Author.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{count}"
            count += 1
        return slug

    def save(self, *args, **kwargs):
        """Slugni avtomatik yaratish va validatsiyani chaqirish."""
        if not self.slug:
            self.slug = self.get_unique_slug()
        self.full_clean()  # `clean` metodini chaqirish
        super().save(*args, **kwargs)

    def __str__(self):
        """Admin panel va boshqa joylarda ko‘rinadigan string."""
        return f"{self.first_name} {self.last_name} ({self.birth_date if self.birth_date else 'No Birthdate'})"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
