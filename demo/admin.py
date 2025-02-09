from django.contrib import admin
from .models import Author, Book, CompanyInfo

admin.site.register(Author)
admin.site.register(CompanyInfo)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'summary')


