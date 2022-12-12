from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

def profile_photo_upload(instance, filename):
    return f"user_{instance.user.id}/{filename}"

class User(AbstractUser):
    user_photo = models.ImageField(upload_to=profile_photo_upload, default="defaults/profile-placeholder.jpg")

