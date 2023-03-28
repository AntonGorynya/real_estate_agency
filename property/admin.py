from django.contrib import admin
from django.contrib.auth.models import User


from .models import Flat, Complaint


class ComplaintForm(admin.ModelAdmin):
    raw_id_field = ['flat']


class FlatForm(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']


admin.site.register(Flat, FlatForm)
admin.site.register(Complaint, ComplaintForm)