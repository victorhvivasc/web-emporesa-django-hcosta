from django.contrib import admin
from .models import service

class ServicesAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
# Register your models here.
admin.site.register(service, ServicesAdmin)