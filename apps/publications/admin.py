from django.contrib import admin

# Register your models here.
from apps.publications.models import Publication, PublicationCategory


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    pass

@admin.register(PublicationCategory)
class PublicationAdmin(admin.ModelAdmin):
    pass

