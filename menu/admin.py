from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    fields = ('name', 'parent', 'named_url', 'url', 'order')
    fk_name = 'menu'

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    list_display = ('name',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'parent', 'get_url', 'order')
    list_filter = ('menu',)
    search_fields = ('name', 'menu__name')
    list_editable = ('order',)
    
    def get_url(self, obj):
        return obj.get_url()
    get_url.short_description = 'URL'