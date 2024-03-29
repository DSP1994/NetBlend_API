from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True)
    event_link = models.URLField('Event URL', max_length=400, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Order events by date of event.
        """
        ordering = ['-date']

    def __str__(self):
        return f'{self.title} {self.date}'
