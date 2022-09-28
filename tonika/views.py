from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import json
import os
from django.conf import settings


def hello(request):
    return render(request, 'index.html', {'data': {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})


def GetSongs(request):
    return render(request, 'songs.html', {'data': {
        'current_date': date.today(),
        'songs': [
            {'title': 'Дождь', 'author': 'ДДТ', 'id': 1},
            {'title': 'Smells Like Teen Spirit', 'author': 'Nirvana', 'id': 2},
            {'title': 'Seven Nation Army', 'author': 'The White Stripes', 'id': 3},
        ]
    }})


def GetSong(request, id):
    with open(os.path.join(settings.BASE_DIR, "tempdb.json"), 'r', encoding='utf-8') as tempdb:
        data = json.load(tempdb)
    song_title = 'title'
    song_author = 'author'
    song_chords = 'text'
    for song in data.get("songs"):
        if song.get("id") == id:
            song_title = song.get("title")
            song_author = song.get("author")
            song_chords = song.get("chords")

    return render(request, 'song.html', {'data': {
        'current_date': date.today(),
        'id': id,
        'title': song_title,
        'author': song_author,
        'chords': song_chords,
        'cover_path': 'covers/cover_' + str(id) + '.jpg'
    }})
