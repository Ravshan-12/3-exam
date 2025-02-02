from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # Sana va vaqt
    updated_at = models.DateTimeField(auto_now=True)      # So‘nggi o‘zgarish vaqti

    class Meta:
        abstract = True  # Abstrakt model, jadval yaratmaydi
