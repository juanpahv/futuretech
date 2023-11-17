from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    creationDate = models.DateField(auto_now_add=True)
    profilePicture = models.BinaryField(null=True)
