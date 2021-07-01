from django.contrib import admin
from .models import Plans
# Register your models here.


@admin.register(Plans)
class PlansModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'item']
