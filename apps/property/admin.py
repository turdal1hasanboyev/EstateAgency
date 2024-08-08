from django.contrib import admin

from apps.property.models import Amenites, Property


@admin.register(Amenites)
class AmenitesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    list_display = ("id", "name", "price", "type", "agent", "status", "area", 'created_at')
