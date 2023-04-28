# from django.contrib import admin
# # from .models import Menu
#
#
# class MenuAdmin(admin.ModelAdmin):
#     list_display = ('name', 'parent', 'url', 'named_url')
#
#
#
# # admin.site.register(Menu, MenuAdmin)
from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'parent')
