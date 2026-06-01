from django.contrib import admin
from .models import (
    Cidade, Ocupacao, Especialidade, Categoria, Turno, Produto,
    Cliente, Profissional, Unidade, Servico, TurnoTrabalho,
    Agendamento, FichaEvolucao, AvaliacaoServico
)

admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(Especialidade)
admin.site.register(Categoria)
admin.site.register(Turno)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Profissional)
admin.site.register(Unidade)
admin.site.register(Servico)
admin.site.register(TurnoTrabalho)
admin.site.register(Agendamento)
admin.site.register(FichaEvolucao)
admin.site.register(AvaliacaoServico)