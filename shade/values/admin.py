from django.contrib import admin
from .models import ShadeVariation

class ValueDisplay(admin.ModelAdmin):
    list_display = [f.name for f in ShadeVariation._meta.fields]
    class Meta:
        model = ShadeVariation

# Register your models here.

admin.site.register(ShadeVariation, ValueDisplay)
