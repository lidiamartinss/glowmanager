from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Cliente, Profissional, Servico, Agendamento, 
    AvaliacaoServico, Categoria, Cidade, Especialidade, 
    FichaEvolucao, Ocupacao, Produto, TurnoTrabalho, Turno, Unidade
)
from .forms import ClienteForm, ProfissionalForm, ServicoForm, AgendamentoForm

# 1. Requisito: Página Inicial
@login_required
def index(request):
    return render(request, 'index.html')

# 2. Requisito: Consulta de Clientes
@login_required
def consulta_clientes(request):
    lista_clientes = Cliente.objects.all()
    return render(request, 'consulta_clientes.html', {'clientes': lista_clientes})

# 3. Requisito: Consulta de Profissionais
@login_required
def consulta_profissionais(request):
    lista_profissionais = Profissional.objects.all()
    return render(request, 'consulta_profissionais.html', {'profissionais': lista_profissionais})

# 4. Requisito: Consulta de Serviços
@login_required
def consulta_servicos(request):
    lista_servicos = Servico.objects.all()
    return render(request, 'consulta_servicos.html', {'servicos': lista_servicos})

# 5. Requisito: Consulta de Agendamentos
@login_required
def consulta_agendamentos(request):
    lista_agendamentos = Agendamento.objects.all()
    return render(request, 'consulta_agendamentos.html', {'agendamentos': lista_agendamentos})



# Requisito: Consulta de Avaliações de Serviços
@login_required
def consulta_avaliacoes(request):
    lista_avaliacoes = AvaliacaoServico.objects.all()
    return render(request, 'consulta_avaliacoes.html', {'avaliacoes': lista_avaliacoes})

# Requisito: Consulta de Categorias
@login_required
def consulta_categorias(request):
    lista_categorias = Categoria.objects.all()
    return render(request, 'consulta_categorias.html', {'categorias': lista_categorias})

# Requisito: Consulta de Cidades
@login_required
def consulta_cidades(request):
    lista_cidades = Cidade.objects.all()
    return render(request, 'consulta_cidades.html', {'cidades': lista_cidades})

# Requisito: Consulta de Especialidades
@login_required
def consulta_especialidades(request):
    lista_especialidades = Especialidade.objects.all()
    return render(request, 'consulta_especialidades.html', {'especialidades': lista_especialidades})

# Requisito: Consulta de Ficha de Evoluções
@login_required
def consulta_fichas(request):
    lista_fichas = FichaEvolucao.objects.all()
    return render(request, 'consulta_fichas.html', {'fichas': lista_fichas})

# Requisito: Consulta de Ocupações
@login_required
def consulta_ocupacoes(request):
    lista_ocupacoes = Ocupacao.objects.all()
    return render(request, 'consulta_ocupacoes.html', {'ocupacoes': lista_ocupacoes})

# Requisito: Consulta de Produtos
@login_required
def consulta_produtos(request):
    lista_produtos = Produto.objects.all()
    return render(request, 'consulta_produtos.html', {'produtos': lista_produtos})

# Requisito: Consulta de Turno de Trabalhos
@login_required
def consulta_turno_trabalhos(request):
    lista_turno_trabalhos = TurnoTrabalho.objects.all()
    return render(request, 'consulta_turno_trabalhos.html', {'turno_trabalhos': lista_turno_trabalhos})

# Requisito: Consulta de Turnos
@login_required
def consulta_turnos(request):
    lista_turnos = Turno.objects.all()
    return render(request, 'consulta_turnos.html', {'turnos': lista_turnos})

# Requisito: Consulta de Unidades
@login_required
def consulta_unidades(request):
    lista_unidades = Unidade.objects.all()
    return render(request, 'consulta_unidades.html', {'unidades': lista_unidades})


# --- SUAS FUNÇÕES DE EXCLUSÃO E EDIÇÃO (MANTIDAS IGUAIS) ---

# 6. Requisito: Excluir Cliente
@login_required
def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('consulta_clientes')

# 7. Requisito: Excluir Profissional
@login_required
def excluir_profissional(request, pk):
    profissional = get_object_or_404(Profissional, pk=pk)
    profissional.delete()
    return redirect('consulta_profissionais')

# 8. Requisito: Excluir Serviço
@login_required
def excluir_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    servico.delete()
    return redirect('consulta_servicos')

# 9. Requisito: Excluir Agendamento
@login_required
def excluir_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    agendamento.delete()
    return redirect('consulta_agendamentos')

# 10. Requisito: Editar Cliente
@login_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('consulta_clientes')
    return render(request, 'form_edicao.html', {'form': form, 'titulo': 'Editar Cliente'})

# 11. Requisito: Editar Profissional
@login_required
def editar_profissional(request, pk):
    profissional = get_object_or_404(Profissional, pk=pk)
    form = ProfissionalForm(request.POST or None, instance=profissional)
    if form.is_valid():
        form.save()
        return redirect('consulta_profissionais')
    return render(request, 'form_edicao.html', {'form': form, 'titulo': 'Editar Profissional'})

# 12. Requisito: Editar Serviço
@login_required
def editar_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    form = ServicoForm(request.POST or None, instance=servico)
    if form.is_valid():
        form.save()
        return redirect('consulta_servicos')
    return render(request, 'form_edicao.html', {'form': form, 'titulo': 'Editar Serviço'})

# 13. Requisito: Editar Agendamento
@login_required
def editar_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    form = AgendamentoForm(request.POST or None, instance=agendamento)
    if form.is_valid():
        form.save()
        return redirect('consulta_agendamentos')
    return render(request, 'form_edicao.html', {'form': form, 'titulo': 'Editar Agendamento'})