from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Consultas
    path('clientes/', views.consulta_clientes, name='consulta_clientes'),
    path('profissionais/', views.consulta_profissionais, name='consulta_profissionais'),
    path('servicos/', views.consulta_servicos, name='consulta_servicos'),
    path('agendamentos/', views.consulta_agendamentos, name='consulta_agendamentos'),
    
    # Exclusões
    path('clientes/excluir/<int:pk>/', views.excluir_cliente, name='excluir_cliente'),
    path('profissionais/excluir/<int:pk>/', views.excluir_profissional, name='excluir_profissional'),
    path('servicos/excluir/<int:pk>/', views.excluir_servico, name='excluir_servico'),
    path('agendamentos/excluir/<int:pk>/', views.excluir_agendamento, name='excluir_agendamento'),

    # Edições (Adicione essas 4 linhas agora!)
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('profissionais/editar/<int:pk>/', views.editar_profissional, name='editar_profissional'),
    path('servicos/editar/<int:pk>/', views.editar_servico, name='editar_servico'),
    path('agendamentos/editar/<int:pk>/', views.editar_agendamento, name='editar_agendamento'),
]