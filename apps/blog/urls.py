from django.urls import path

from .views import blog, blog_single


urlpatterns = [
    path("blog/", blog, name="blog"),
    path("blog-single/<slug:slug>/", blog_single, name="blog-single"),
]
