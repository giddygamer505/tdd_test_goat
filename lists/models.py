from django.db import models

class Item(models.Model):
    text = models.TextField()
    priority = models.TextField(default='Low')