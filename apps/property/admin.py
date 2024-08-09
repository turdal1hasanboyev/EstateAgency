from django.contrib import admin

from apps.property.models import Amenities, Property


@admin.register(Amenities)
class AmenitiesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "property", "created_at")


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    list_display = ("id", "name", "price", "type", "agent", "status", "area", 'created_at')
