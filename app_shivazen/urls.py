from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shivazen'  # Adicione esta linha para o namespace

urlpatterns = [
    path('', views.home, name='inicio'),  # URL raiz agora aponta para home
    path('agenda/agendamento/', views.agendaCadastro, name='agendaCadastro'),
    path('agenda/contato/', views.agendaContato, name='agendaContato'),
    path('usuario/cadastro/', views.usuarioCadastro, name='usuarioCadastro'),
    path('usuario/login/', views.usuarioLogin, name='usuarioLogin'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)