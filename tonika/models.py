from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'authors'


class Song(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    chords = models.CharField(max_length=10000)

    class Meta:
        managed = True
        db_table = 'songs'


class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    favourites = models.ManyToManyField(Song)

    class Meta:
        managed = True
        db_table = 'users'
