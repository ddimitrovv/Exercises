from django.contrib import admin

from Car_Collection_App.web.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...
