from django.db import models

from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class User(BaseModel, AbstractUser):
    bio = RichTextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.username}"
    