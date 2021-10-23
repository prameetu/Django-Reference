from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
# Create your models here.

class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User)

    #additional classes
    protfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.username