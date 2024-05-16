from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    contents=models.CharField(max_length=100)
    createdtime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contents
    
