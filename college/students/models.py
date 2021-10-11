from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=264)
    roll = models.IntegerField()
    dob = models.DateField()
    email = models.EmailField()
    verify_email = models.EmailField()