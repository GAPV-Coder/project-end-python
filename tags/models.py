from django.db import models
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name