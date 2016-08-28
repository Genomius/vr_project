from django.contrib import admin
from models import Main


class MainAdmin(admin.ModelAdmin):
    list_display = ("spent_money", "earned_money", "sold_all")


#admin.site.register(Main, MainAdmin)










