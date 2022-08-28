from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Contact, Reports

admin.site.site_header  =  "Ede Capital Admin"  
admin.site.site_title  =  "Ede Capital Admin"
admin.site.index_title  =  "Ede Capital Admin"

# Register your models here.

class ContactAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'subject', 'phonenumber', 'email', 'message']

class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'download_link','created_on')
    list_filter = ("created_on",)
    search_fields = ['title', 'summary']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Reports, ReportAdmin)

