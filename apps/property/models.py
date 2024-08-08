from django.db import models

import uuid
from django.template.defaultfilters import slugify 
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

from apps.common.models import BaseModel
from apps.agent.models import Agent


STATUS = (
    (0, _("in_the_living")),
    (1, _("sale")),
    (2, _("rent")),
)


class Property(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=225, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    location = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(upload_to='properties/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    type = models.CharField(max_length=225, null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
    status = models.IntegerField(default=None, choices=STATUS, null=True, blank=True)
    area = models.IntegerField(default=0, null=True, blank=True)
    beds = models.IntegerField(default=0, null=True, blank=True)
    boths = models.IntegerField(default=0, null=True, blank=True)
    garage = models.IntegerField(default=0, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("property-single", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"

        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{ self.id } - { self.name }"


class Amenities(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    property = models.ManyToManyField(Property, blank=True)

    def __str__(self) -> str:
        return f"{ self.id } - { self.name }"
 