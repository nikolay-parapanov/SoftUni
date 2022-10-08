import random

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

class Student:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_info(self):
        return f'Name: {self.name}; Age: {self.age}'


def index(request):
    context = {
        'title': 'SoftUni Homepage',
        'value': random.random(),
        'info': {
            'address': 'Sofia',
        },
        'student': Student('Doncho', 19),
        'students': ['Ivan','Pesho', 'Mariya'],
        # 'students': []
        'values': list(range(20))
    }

    return render(request, 'index.html', context)

def redirect_to_home(request):
    return redirect('index')

def about(request):
    return render(request, 'about.html')