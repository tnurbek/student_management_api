from django.db import models
from utils.models import Timestamp

class Certificate(Timestamp, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name.lower()