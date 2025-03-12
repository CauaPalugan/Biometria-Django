from django.shortcuts import render, redirect
from .forms import FuncionarioForm

def cadastro(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('firstLogin')  
    else:
        form = FuncionarioForm()
    
    return render(request, 'cadastro.html', {'form': form})

def firstLogin(request):
    return render(request, 'firstLogin.html')
