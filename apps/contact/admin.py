from django.contrib import admin

from .models import Contact, AgentContact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')


@admin.register(AgentContact)
class AgentContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'agent', 'name', 'email', 'created_at')
