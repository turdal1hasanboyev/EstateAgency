from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(unique=True, max_length=225, null=True, blank=True)
    subject = models.CharField(max_length=225, null=True, blank=True)
    message = RichTextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{ self.id } - { self.name }"


class AgentContact(BaseModel):
    agent = models.ForeignKey("agent.Agent", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(unique=True, max_length=225, null=True, blank=True)
    message = RichTextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{ self.id } - { self.agent }"
