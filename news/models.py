from django.db import models

# Create your models here.


class NewOnSite(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.FloatField('Price (NZD)')

    created = models.DateTimeField('Created', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Updated', auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title
