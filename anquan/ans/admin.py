from django.contrib import admin
from .models import An 

@admin.register(An)
class AnAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']
    list_filter = ['id']