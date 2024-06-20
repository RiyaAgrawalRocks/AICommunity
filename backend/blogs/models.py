from django.db import models
import uuid

class blog(models.Model):
    title=models.CharField(max_length=100, default=None)
    authors=models.CharField(max_length=100, default=None)
    content=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
