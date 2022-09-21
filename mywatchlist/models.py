from django.db import models

# Create your models here.
class watchList(models.Model):
    watched = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    rating = models.IntegerField()
    release_date = models.CharField(max_length = 50)
    review = models.TextField()