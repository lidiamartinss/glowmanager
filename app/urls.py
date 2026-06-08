from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('clientes/', views.consulta_clientes, name='consulta_clientes'),
    path('profissionais/', views.consulta_profissionais, name='consulta_profissionais'),
    path('servicos/', views.consulta_servicos, name='consulta_servicos'),
    path('agendamentos/', views.consulta_agendamentos, name='consulta_agendamentos'),
    
    path('avaliacaoservicos/', views.consulta_avaliacoes, name='consulta_avaliacoes'),
    path('categorias/', views.consulta_categorias, name='consulta_categorias'),
    path('cidades/', views.consulta_cidades, name='consulta_cidades'),
    path('especialidades/', views.consulta_especialidades, name='consulta_especialidades'),
    path('fichaevolucoes/', views.consulta_fichas, name='consulta_fichas'),
    path('ocupacoes/', views.consulta_ocupacoes, name='consulta_ocupacoes'),
    path('produtos/', views.consulta_produtos, name='consulta_produtos'),
    path('turnotrabalhos/', views.consulta_turno_trabalhos, name='consulta_turno_trabalhos'),
    path('turnos/', views.consulta_turnos, name='consulta_turnos'),
    path('unidades/', views.consulta_unidades, name='consulta_unidades'),
    
    path('clientes/excluir/<int:pk>/', views.excluir_cliente, name='excluir_cliente'),
    path('profissionais/excluir/<int:pk>/', views.excluir_profissional, name='excluir_profissional'),
    path('servicos/excluir/<int:pk>/', views.excluir_servico, name='excluir_servico'),
    path('agendamentos/excluir/<int:pk>/', views.excluir_agendamento, name='excluir_agendamento'),

    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('profissionais/editar/<int:pk>/', views.editar_profissional, name='editar_profissional'),
    path('servicos/editar/<int:pk>/', views.editar_servico, name='editar_servico'),
    path('agendamentos/editar/<int:pk>/', views.editar_agendamento, name='editar_agendamento'),
]