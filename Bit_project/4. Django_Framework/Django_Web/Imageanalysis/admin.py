from django.contrib import admin
from .models import mage2


# Register your models here.

class MageAdmin(admin.ModelAdmin):
    list_display = 'text'


admin.site.register(mage2)
