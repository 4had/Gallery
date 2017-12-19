from django.contrib import admin
from .models import *


class ItemImageinline(admin.TabularInline):
    model = ItemImage
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Item._meta.fields]
    inlines = [ItemImageinline]
    class Meta:
        model = Item


class ItemImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ItemImage._meta.fields]

    class Meta:
        model = ItemImage



admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage, ItemImageAdmin)
admin.site.register(Comment)