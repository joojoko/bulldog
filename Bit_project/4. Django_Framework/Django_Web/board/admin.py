from .models import Board
from django.contrib import admin
# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Board, BoardAdmin)
