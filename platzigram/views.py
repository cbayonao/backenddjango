"""
Module from views
"""
# Django HttpResponse
from django.http import HttpResponse, response
from django.http import JsonResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    """
    docstring
    """
    # '%b(Mes) %d(dia)th, %Y(año) - %H(horas):%M(minutos) hrs'
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh! Hi, Current server time is: {now}')

def sorted(request):
    """
    My solution for the task
    """
    # import pdb; pdb.set_trace()
    numbers = sorted([int(number) for number in request.GET['numbers'].split(',')])
    return JsonResponse(numbers, safe=False)


def TeacherHi(request):
    """
    Solution for teacher
    """
    numbers = request.GET['numbers'].split(',')
    numbers = [int(number) for number in numbers]
    numbers = sorted(numbers)
    data = {
        'status': 'Ok',
        'numbers': numbers,
        'message': 'Succesfully sorted numbers',
    }
    return HttpResponse(json.dumps(data, indent=2), content_type='application/json')

def sayHi(request, name, age):
    """
    Return a greeting and verification for user age
    """
    if age < 12:
        message = f'Sorry {name}, you are not allowed here!'
    else:
        message = f'Hello {name}, welcome to Platzigram!'
    return HttpResponse(message)
    