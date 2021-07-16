from django.db import models
from users.models import User
from tags.models import Tag

# Create your models here.
class Newsletter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='assets/newsletters')
    meta = models.CharField(max_length=30)
    frequency = models.IntegerField()
    creationDate = models.DateTimeField(auto_now_add=True)

    users = models.ManyToManyField(User, related_name='users')
    tags = models.ManyToManyField(Tag, related_name='tags')

    def __str__(self):
        return self.name