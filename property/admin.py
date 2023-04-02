from django.contrib import admin
from django.contrib.auth.models import User


from .models import Flat, Complaint, Owner


class AdminInline(admin.StackedInline):
    model = Flat.owners.through
    raw_id_fields = ['owner']


@admin.register(Owner)
class OwnerForm(admin.ModelAdmin):
    raw_id_fields = ['owners_flats']


@admin.register(Complaint)
class ComplaintForm(admin.ModelAdmin):
    raw_id_fields = ['flat']

@admin.register(Flat)
class FlatForm(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['likes', 'owners']
    inlines = [AdminInline]
