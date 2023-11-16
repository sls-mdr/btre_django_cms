from django.db import models
from django.utils import timezone


class Contact(models.Model):
    listing = models.CharField(max_length=255)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=timezone.now, blank=True)
    realtor_email = models.CharField(max_length=100)
    # Inquieries can be send by not registered users
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
