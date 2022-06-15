from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('type',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('tag',)}


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ContentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Content, ContentAdmin)
