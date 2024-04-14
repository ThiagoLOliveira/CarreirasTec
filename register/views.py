from django.shortcuts import render
from .models import dados_usuarios

# Create your views here.
def reg(request):
    return render(request, 'register\signup.html')

def cad(request):
    #cadastrar os usuarios
    novo_usuario = dados_usuarios()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()