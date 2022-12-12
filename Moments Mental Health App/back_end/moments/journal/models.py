from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

def entry_photo_upload(instance, filename):
    return f"user_{instance.owner.id}/entries/{filename}"


def moment_photo_upload(instance, filename):
    return f"user_{instance.owner.id}/moments/{filename}"


class Prompt(models.Model):
    prompt = models.CharField(max_length=200)

    def __str__(self):
        return self.prompt

class Entry(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to=entry_photo_upload, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entries")
    prompt = models.ForeignKey("Prompt", on_delete=models.RESTRICT, related_name="entries", blank=True, null=True)

    def __str__(self):
        return f"({self.pk}) {self.owner.username} - {self.title}"

    class Meta:
        verbose_name_plural = "Entries"

class Moment(models.Model):
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to=moment_photo_upload, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="moments")

    def __str__(self):
        return f"({self.pk}) {self.owner.username} - {self.description}"