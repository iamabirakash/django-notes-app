from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    is_publish = models.BooleanField(default=True)
