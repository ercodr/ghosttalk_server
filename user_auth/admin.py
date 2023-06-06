from django.contrib import admin
from .models import AuthToken

class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'token']

admin.site.register(AuthToken, AuthTokenAdmin)
