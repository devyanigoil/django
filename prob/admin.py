from django.contrib import admin

# Register your models here
from .models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)