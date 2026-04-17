from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    

# Create your models here.
