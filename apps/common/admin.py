from django.contrib import admin

from apps.common.models import Service, Testimonials


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('id', "male_name", "female_name", 'created_at')
