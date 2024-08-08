from django.contrib import admin

from apps.blog.models import Category, Comment, Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'name', 'email', 'website', 'user', 'created_at')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "category", "created_at")
    prepopulated_fields = {"slug": ["name"]}
