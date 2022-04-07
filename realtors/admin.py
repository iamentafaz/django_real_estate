from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = list(('name', 'phone', 'email'))
    list_display_links = ('phone', 'name')
    search_fields = ('name',)
    list_per_page = 12

# Register your models here.

admin.site.register(Realtor, RealtorAdmin)