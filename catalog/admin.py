from django.contrib import admin
from .models import Foto


class FotoAdminModel(admin.ModelAdmin):
    fieldsets = [
        ('О фотографии', {'fields': ['name', 'text', 'image', 'date_added',]})
    ]
    list_display = ['name', 'text', 'date_added',]
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Foto, FotoAdminModel)
