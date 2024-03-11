from django.db import models

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
    organizations = models.ManyToManyField(Organization)
    image = models.ImageField(upload_to ='uploads/', blank=True)
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title


