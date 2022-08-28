from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Contact, Reports, Team

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

class TeamAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'position')
    list_filter = ("hierarchy",)
    search_fields = ['fullname', 'position']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Reports, ReportAdmin)
admin.site.register(Team, TeamAdmin)


