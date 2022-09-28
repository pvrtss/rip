from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import json
import os
from django.conf import settings

from tonika.models import Song


def hello(request):
    return render(request, 'index.html', {'data': {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})


def GetSongs(request):
    return render(request, 'songs.html', {'data': {
        'current_date': date.today(),
        'songs': Song.objects.all()
    }})


def GetSong(request, id):
    song = Song.objects.filter(id=id)[0]
    return render(request, 'song.html', {'data': {
        'current_date': date.today(),
        'id': id,
        'title': song.name,
        'author': song.author.name,
        'chords': song.chords,
        'cover_path': 'covers/cover_' + str(id) + '.jpg'
    }})
