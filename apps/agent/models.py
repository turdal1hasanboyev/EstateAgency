from django.db import models

import uuid
from django.template.defaultfilters import slugify 
from django.urls import reverse
from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Agent(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=225)
    image = models.ImageField(upload_to='agents/', null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True, max_length=225)
    email_2 = models.EmailField(unique=True, null=True, blank=True, max_length=225)
    phone = models.CharField(null=True, blank=True, max_length=225)
    skype = models.CharField(null=True, blank=True, max_length=225)
    mobile_phone = models.CharField(null=True, blank=True, max_length=225)

    def get_absolute_url(self):
        return reverse("agent-single", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{ self.id } - { self.name }"
    