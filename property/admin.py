from django.contrib import admin
from django.contrib.auth.models import User


from .models import Flat, Complaint, Owner


class AdminInline(admin.StackedInline):
    model = Flat.owner_set.through
    raw_id_fields = ['owner']


class OwnerForm(admin.ModelAdmin):
    raw_id_fields = ['owners_flats']


class ComplaintForm(admin.ModelAdmin):
    raw_id_fields = ['flat']


class FlatForm(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owners']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['likes']
    inlines = [AdminInline]


admin.site.register(Flat, FlatForm)
admin.site.register(Complaint, ComplaintForm)
admin.site.register(Owner, OwnerForm)
