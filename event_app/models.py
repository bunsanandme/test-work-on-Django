from django.db import models
from django.utils.timezone import now

class Organization(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    address = models.CharField(max_length=50)
    postcode = models.IntegerField()

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    organizations = models.ManyToManyField(Organization, through='OrganizationEvent', blank=True, null=True)
    image = models.ImageField(upload_to ='uploads/', blank=True)
    date = models.DateField(default=now)

    def __str__(self):
        return self.title
    
class OrganizationEvent(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.organization} {self.event}' 


