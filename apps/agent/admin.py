from django.contrib import admin

from apps.agent.models import Agent


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'email_2', 'phone', 'mobile_phone', 'created_at')
    prepopulated_fields = {"slug": ["name"]}
