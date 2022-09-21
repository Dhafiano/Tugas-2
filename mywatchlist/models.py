from django.db import models

class BarangWatchList(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()
# Create your models here.
