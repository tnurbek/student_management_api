from django.db import models
from utils.models import Timestamp

class Lecture(Timestamp, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    slides_url = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    notes = models.TextField()

