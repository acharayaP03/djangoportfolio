from django.db import models

class About(models.Model):
    image = models.ImageField(upload_to="images/")
    headline = models.CharField(max_length=255)
    summary = models.TextField()
