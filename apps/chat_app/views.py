#  Dajango
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request, 'index.html')


def chat(request):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('index'))
    else:
        name = request.POST.get('email')
        return render(request, 'chat.html', {'nombre': name})


def loginView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email.lower()).username
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'chat.html', {'nombre': email})
        else:
            return render(request, 'index.html', {'error': 'Usuario o Password incorrectos'})
    return render(request, 'index.html')


def registerView(request):
    if request.method == 'POST':
        name = request.POST['name']
        last = request.POST['last']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=email, password=password, email=email,
                                            first_name=name, last_name=last)
        except IntegrityError:
            return render(request, 'register.html', {'error': 'Usuario ya existe'})

        return render(request, 'index.html')

    return render(request, 'register.html')
