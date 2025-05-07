from django.shortcuts import render

def home(request):
    return render(request, 'inicio/home.html')

def agendaCadastro(request):
    return render(request, 'agenda/agendamento.html')

def agendaContato(request):
    return render(request, 'agenda/contato.html')

def usuarioLogin(request):
    return render(request, 'usuario/login.html')

def usuarioCadastro(request):
    return render(request, 'usuario/cadastro.html')  # Corrigi o caminho do template