"""Docstring"""
# from django.http import HttpResponse
from django.shortcuts import render

# Utilis
from datetime import datetime

# Local
import posts

posts = [
    {
        'title': 'Bayona city',
        'author': {
            'name': 'Andreina',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'url_picture': 'https://picsum.photos/200/200/?image=1036',
        'content': 'content bayona city'
    },
    {
        'title': 'Via lactea',
        'author': {
            'name': 'cvander',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'url_picture': 'https://picsum.photos/200/200/?image=903',
        'content': 'content via lactea'
    },
    {
        'title': 'Nuevo auditorio',
        'author': {
            'name': 'jdaroesti',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'url_picture': 'https://picsum.photos/200/200/?image=1076',
        'content': 'content'
    },
]

def list_posts(request):
    """
    docstring
    """
    return render(request, '../templates/posts/feed.html', {'posts': posts})