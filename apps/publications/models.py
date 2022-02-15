from django.db import models
from django.utils import timezone
# Create your models here.


class PublicationCategory(models.Model):
    """Модель для сущности категории"""
    title = models.CharField(max_length=75)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

class Publication(models.Model):
    """Модель для сущности публикации"""
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(to=PublicationCategory, on_delete=models.CASCADE, related_name="publications")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return self.title