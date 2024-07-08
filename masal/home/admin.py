from django.contrib import admin
from .models import Masal
# Register your models here.

class MasalAdmin(admin.ModelAdmin):
    list_display = ['id','name','date','isPublished']
    list_display_links = ['name']
    list_filter = ['date','isPublished']
    list_editable = ['isPublished']
    search_fields = ['name']
    
admin.site.register(Masal,MasalAdmin)
