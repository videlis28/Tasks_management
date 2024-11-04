from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255, default='Default Task Name')

    def __str__(self):
        return self.name
