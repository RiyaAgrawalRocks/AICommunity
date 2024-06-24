from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=100, default=None)
    authors=models.CharField(max_length=100, default=None)
    content=models.TextField()
    date=models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

class Member(models.Model):
    name=models.CharField(max_length=100, default=None)
    position=models.CharField(max_length=100, default=None)
    email=models.EmailField(max_length=100, default=None)
    phone=models.CharField(max_length=100, default=None)
    linkedin=models.URLField(max_length=100, default=None)
    github=models.URLField(max_length=100, default=None)
    pic=models.ImageField(upload_to= 'media\images', default=None)

    def __str__(self):
        return self.name
