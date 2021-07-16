from django.db import models
from users.models import User
from newsletters.models import Newsletter
from datetime import datetime

# Create your models here.
class Vote(models.Model):
    updatedAt = models.DateTimeField(auto_now=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
