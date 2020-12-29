from django.db import models

# Create Blog Model.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to= 'image/')
