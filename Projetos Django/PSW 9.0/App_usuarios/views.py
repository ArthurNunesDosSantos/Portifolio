from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth
def cadastro(request):
    if request.method == "GET": 
        return render(request, 'cadastro.html')
    elif request.method =="POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirma_senha = request.POST.get('confirmar_senha')

        if len(username.strip()) == 0 or len(senha.strip()) == 0 or len(confirma_senha.strip()) == 0:
                messages.add_message(request, constants.ERROR,'Preencha os campos corretamente!')
                return redirect('/usuarios/cadastro')
        if not senha == confirma_senha:
             messages.add_message(request, constants.ERROR,'Senha diferente da Confirmar senha!')
             return redirect('/usuarios/cadastro')
        
        user =  User.objects.filter(username = username)

        if user.exists():
             messages.add_message(request,constants.ERROR,'Usuario ja existe!')
             return redirect('/usuarios/cadastro')

        try:
            User.objects.create_user(
            username= username,
            password= senha
            
             )
            return redirect('/usuarios/logar')
        except:
            messages.add_message(request, constants.ERROR,'Erro interno do servidor!')
            return redirect('/usuarios/cadastro')

def logar(request):
    if request.method =='GET':
        return render(request,'login.html')
    elif request.method =="POST": 
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = auth.authenticate(request, username=username , password = senha)
        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS,'Login Concluido!')
            return redirect('/flashcard/novo_flashcard/')
        else:
            messages.add_message(request, constants.ERROR,'Login Invalido!')
            return redirect('/usuarios/logar/')
  
def logout(request):
    auth.logout(request)
    return redirect('usuarios/logar')
