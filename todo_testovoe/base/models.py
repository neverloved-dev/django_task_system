from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.IntegerField("id",primary_key=True,unique=True)
    title = models.CharField("title",max_length=100)
    is_completed = models.BooleanField("is_completed",default=False)