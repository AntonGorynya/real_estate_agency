from django.contrib import admin


from .models import Flat


class Admin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']


admin.site.register(Flat, Admin)
# admin.site.register(Flat)