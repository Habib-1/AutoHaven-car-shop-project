from django.contrib import admin
from .models import purchase
# Register your models here.

class purchaseAdmin(admin.ModelAdmin):
    list_display=['user','product','purchased_at',]

admin.site.register(purchase,purchaseAdmin)