from django.db import models
from django.contrib.auth.models import User
import secrets

class AuthToken(models.Model):
    user = models.OneToOneField(User, to_field="username", on_delete=models.CASCADE)
    token = models.TextField(default=secrets.token_hex(16))
    
    def __str__(self) -> str:
        return self.user.username