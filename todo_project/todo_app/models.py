from django.db import models
from django.urls import reverse
from datetime import datetime
# Create your models here.

class ToDos(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Yazar', related_name='posts')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    finished = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title   
