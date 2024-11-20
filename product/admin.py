from django.contrib import admin
from .models import car,brand,Comments
# Register your models here.
admin.site.register(car)
# 
class brandAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('brand_name',)}
    list_display=['brand_name','slug',]
admin.site.register(brand,brandAdmin)
admin.site.register(Comments)