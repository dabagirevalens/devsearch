from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save, post_delete


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        blank=True, null=True, upload_to='profiles/', default='profiles/user-default.png')
    social_github = models.CharField(max_length=100, null=True, blank=True)
    social_linkedin = models.CharField(max_length=100, null=True, blank=True)
    social_twiter = models.CharField(max_length=100, null=True, blank=True)
    social_youtube = models.CharField(max_length=100, null=True, blank=True)
    social_website = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


def profileUpdated(sender, instance, created, **kwargs):
    print("Profile Saved!")
    print("Instance: ", instance)
    print("Created: ", created)


def deleteUser(sender, instance, **kwargs):
    print("Deleting user...")


post_save.connect(profileUpdated, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
