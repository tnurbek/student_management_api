from django.db import models
from utils.models import Timestamp

class WaitlistEntry(Timestamp, models.Model):
    fname = models.CharField(max_length=100, verbose_name='first name')
    lname = models.CharField(max_length=100, verbose_name='last name')
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    level = models.IntegerField(verbose_name='Class Level')
    notes = models.TextField()

    def __str__(self):
        return self.fname.lower()+'_'+self.lname.lower()

    def full_name(self):
        return f'{self.fname} {self.lname}'

    class Meta:
        verbose_name_plural = 'Waitlist entries'