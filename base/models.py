from django.db import models

# Create your models here.

class Article_model(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()