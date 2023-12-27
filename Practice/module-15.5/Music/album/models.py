from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_release_date = models.DateField()
    RATE =  [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')]
    album_rating = models.IntegerField(choices=RATE)

    def __str__(self):
        return self.album_name