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
    tratamentos_faciais = [
        {'nome': 'Bioestimuladores de colágeno', 'descricao': 'Rejuvenesce sua pele, aumentando a firmeza e elasticidade e reduzindo rugas.'},
        # Adicione todos os outros tratamentos faciais aqui
    ]
    
    tratamentos_corporais = [
        {'nome': 'Drenagem linfática manual', 'descricao': 'Reduz inchaço e melhora a circulação para uma pele mais saudável e revitalizada.'},
        # Adicione todos os outros tratamentos corporais aqui
    ]
    
    return render(request, 'inicio/quemsomos.html', {
        'tratamentos_faciais': tratamentos_faciais,
        'tratamentos_corporais': tratamentos_corporais
    })

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
