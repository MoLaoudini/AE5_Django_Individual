from django.contrib import admin
from . import models

@admin.register(models.Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'actividad']