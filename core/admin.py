from django.contrib import admin
from .models import Message, Profile


class MessageAdmin(admin.ModelAdmin):
    list_display = ['profile', 'content', 'created']
    list_filter = ['profile', 'created']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'created']
    list_filter = ['created']
    

admin.site.register(Message, MessageAdmin)
admin.site.register(Profile, ProfileAdmin)