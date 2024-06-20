from django.db import models
import uuid

class blog(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=100, default=None)
    authors=models.CharField(max_length=100, default=None)
    content=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
