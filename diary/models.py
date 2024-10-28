from django.db import models

# Create your models here.
class Note:
    """A diary note added by the user"""
    text = models.CharField(max_length=400)