from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)    
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user.username


class Message(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_messages')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self) -> str:
        return self.profile.user.username