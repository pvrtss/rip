from django.db import models


# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    chords = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'songs'
