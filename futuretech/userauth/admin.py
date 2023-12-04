from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('creationDate',)

admin.site.register(UserProfile, UserProfileAdmin)