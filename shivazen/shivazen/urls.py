from django.urls import path
from app_shivazen import views


urlpatterns = [
    # rota, view responsavel, nome de referencia
    # path('home/', views.home, name='home'),
    path('home/', views.home, name='home'),

    path('usuarios/usuario.html', views.usuarios, name='usuarios'),
    path('usuarios/listausuario.html',
         views.listausuario, name='listagem_usuarios'),
]
