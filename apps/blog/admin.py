from django.contrib import admin

from .models import Category, Comment, Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'name', 'email', 'web_site', 'user', 'created_at')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "author", "category", "created_at")
    prepopulated_fields = {"slug": ["name"]}
