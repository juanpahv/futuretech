from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User)
    user = models.OneToOneField(User)
    creationDate = models.DateTimeField(auto_now_add=True)
    profilePicture = models.BinaryField(null=True)

