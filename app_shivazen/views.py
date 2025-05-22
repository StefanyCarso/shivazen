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
    return render(request, 'usuario/cadastro.html')  

def quemsomos(request):
    return render(request, 'inicio/quemsomos.html') 

def prontuarioconsentimento(request):
    return render(request, 'telas/ProntuarioConsentimento.html') 

def profissionalCadastro(request):
    return render(request, 'telas/tela_cadastro_profissional.html') 
    
def profissionalEditar(request):
    return render(request, 'telas/tela_editar_profissional.html') 

def login(request):
    return render(request, 'telas/tela_login.html') 

def painel(request):
    return render(request, 'telas/tela_painel.html') 
