from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()

    # it will display the first 50 characters of the text field
    def __str__(self):
        return self.text[:50]
