from django.contrib import admin
from .models import LostAndFoundItem


@admin.register(LostAndFoundItem)
class LostAndFoundItemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'item_name', 'category', 'location', 'status', 'date_reported', 'contact_information')
    list_filter = ('status', 'category')
    search_fields = ('item_name', 'description', 'location', 'contact_information')
    list_editable = ('status',)
    ordering = ('-date_reported',)