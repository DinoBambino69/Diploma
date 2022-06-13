from django.contrib import admin
from .models import UserProfiles

@admin.register(UserProfiles)
class ProfileAdmin(admin.ModelAdmin):
    pass
