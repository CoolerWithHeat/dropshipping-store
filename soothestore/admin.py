from django.contrib import admin
from .models import *

admin.site.register(MassageChair)
admin.site.register(ChairComment)
admin.site.register(ChairType)
admin.site.register(ChairFeature)

@admin.register(Brand)
class Brands(admin.ModelAdmin):
    list_display = ('brand_name', 'authorized_in')