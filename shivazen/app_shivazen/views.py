from django.shortcuts import render
from .models import Usuario

# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def usuarios(request):
    return render(request, 'usuarios/usuarios.html')


def listausuario(request):
    # salvar dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # exibir todos os usuarios cadastrados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # retornar os dados para a pagina de listagem
    return render(request, 'usuarios/listausuario.html', usuarios)
