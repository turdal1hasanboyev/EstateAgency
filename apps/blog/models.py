from django.db import models

import uuid
from django.template.defaultfilters import slugify 
from django.urls import reverse
from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=225, null=True, blank=True)

    def __str__(self) -> str:
        return f"{ self.id } - { self.name }"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"

        return super().save(*args, **kwargs)
    

class Tag(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=225, null=True, blank=True)

    def __str__(self) -> str:
        return f"{ self.id } - { self.name }"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"

        return super().save(*args, **kwargs)


class Blog(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    author = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=225, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return f"{ self.id } - { self.name }"
    
    def get_absolute_url(self):
        return reverse("blog-single", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"

        return super().save(*args, **kwargs)


class Comment(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    website = models.URLField(unique=True, null=True, blank=True)
    message = RichTextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{ self.id } - { self.name }"
