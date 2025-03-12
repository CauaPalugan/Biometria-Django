from django.shortcuts import render

def cadastro(request):
    return render(request, 'cadastro.html')

def firstLogin(request):
    return render(request, 'firstLogin.html')
