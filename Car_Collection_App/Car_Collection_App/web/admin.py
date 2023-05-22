from django.contrib import admin

from Car_Collection_App.web.models import Profile, Car


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    ...
