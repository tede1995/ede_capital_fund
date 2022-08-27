from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Contact

admin.site.site_header  =  "Ede Capital Admin"  
admin.site.site_title  =  "Ede Capital Admin"
admin.site.index_title  =  "Ede Capital Admin"

# Register your models here.

class ContactAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'subject', 'phonenumber', 'email', 'message']

admin.site.register(Contact, ContactAdmin)

