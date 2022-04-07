from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'realtor', 'address', 'is_published')
    list_display_links = ('title', 'id')
    list_filter = ('title',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'state', 'zipcode')

# Register your models here.

admin.site.register(Listing, ListingAdmin)

