from django.db import models

from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        

class Service(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return f"{ self.id } - { self.name }"
    

class Testimonials(BaseModel):
    male_name = models.CharField(max_length=225, null=True, blank=True)
    female_name = models.CharField(max_length=225, null=True, blank=True)
    testimonial = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)

    def __str__(self):
        return f"{ self.id } - { self.male_name } - { self.female_name }"
 