from django.shortcuts import render
#from django.http import HttpResponse
import random
import string

content = {
    'home': {'title': 'Home',
             'heading': 'Password generator',
             'range': range(6, 31),
            },
    'password': {'title': 'Password',
                 'heading': 'Password',
                },
    'about': {'title': 'About',
              'heading': 'About',
              'content': '''Этот сайт сделан в качестве домашнего задания. На нём можно сгенерировать пароли различной длинны и сложности, используя символы в верхнем/нижнем регистре, цифры и спецсимволы.'''
              }
}

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', content['home'])

def password(request):
    thepassword = ''
    length = int(request.GET.get('length', '6'))
    characters = list(string.ascii_lowercase)
    
    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('numbers'):
        characters.extend(list(string.digits))
    if request.GET.get('specials'):
        characters.extend(list(string.punctuation))

    for i in range(length):
        thepassword += random.choice(characters)
    content['password']['password'] = thepassword
    
    return render(request, 'generator/password.html', content['password'])

def about(request):
    return render(request, 'generator/about.html', content['about'])