from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zipcode = models.TextField()

    @python_2_unicode_compatible
    def __str__(self):
        return self.street

class Event(models.Model):
    name = models.CharField(max_length=200, default='New Event')
    description = models.CharField(max_length=2000, blank=True)
    date = models.DateTimeField('date hosted')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    @python_2_unicode_compatible
    def __str__(self):
        return str(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=200, default='New Tag')
    events = models.ManyToManyField(Event)

    @python_2_unicode_compatible
    def __str__(self):
        return self.name