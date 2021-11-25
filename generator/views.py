from django.shortcuts import render
#from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    params = {
        'title': 'Home',
        'heading': 'Password generator',
        'range': range(6, 31),
    }
    return render(request, 'generator/home.html', params)

def password(request):
    thepassword = ''
    length = int(request.GET.get('length'))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('specials'):
        characters.extend(list('!@#$%^&*()='))

    for i in range(length):
        thepassword += random.choice(characters)

    params = {
        'title': 'Password',
        'heading': 'Password',
        'password': thepassword,
    }
    return render(request, 'generator/password.html', params)

def about(request):
    params = {
        'title': 'About',
        'heading': 'About',
        'content': '''Этот сайт сделан в качестве домашнего задания. 
        На нём можно сгенерировать пароли различной длинны и сложности, 
        используя символы в верхнем регистре, цифры и спецсимволы.'''
        
    }
    return render(request, 'generator/about.html', params)