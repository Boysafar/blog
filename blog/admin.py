from django.contrib import admin
from .models import BlogSetting, Article, Resume


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('body', 'is_active')

