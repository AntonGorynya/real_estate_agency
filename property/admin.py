from django.contrib import admin
from django.contrib.auth.models import User


from .models import Flat, Complaint, Owner


class OwnerForm(admin.ModelAdmin):
    raw_id_fields = ['owners_flats']


class ComplaintForm(admin.ModelAdmin):
    raw_id_field = ['flat']


class FlatForm(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'owner_pure_phone']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_field = ['likes']


admin.site.register(Flat, FlatForm)
admin.site.register(Complaint, ComplaintForm)
admin.site.register(Owner, OwnerForm)