from django.db import models

# Create Blog Model.
class Blog(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=40)
    created_at = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to= 'image/')

    def __str__(self):
        return self.title
        
    def truncate_body(self):
        return self.body[:200]
    
    def prettify_date(self):
        return self.created_at.strftime('%b %e %Y')