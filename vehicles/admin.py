from django.contrib.admin import ModelAdmin, register
from .models import vehicles

@register(vehicles)
class vehicles(ModelAdmin):
    pass
