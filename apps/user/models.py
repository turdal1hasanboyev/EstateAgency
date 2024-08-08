from django.db import models

from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class User(BaseModel, AbstractUser):
    description = RichTextField(null=True, blank=True)
    profilephoto = models.ImageField(upload_to='profilephotos/', null=True, blank=True)
    phone = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self) -> str:
        return f"{ self.id } - { self.username }"
    

class About(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    bio = RichTextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self) -> str:
        return f"{ self.id } - { self.name }"
