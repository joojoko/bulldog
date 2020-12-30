from .models import Contact
from django.contrib import admin
# Register your models here.


class contactAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Contact, contactAdmin)
