from django.db import models



class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} - {self.uf}"


class Ocupacao(models.Model):
    nome = models.CharField(max_length=100)  # Ex: Esteticista, Biomédica, Recepcionista

    def __str__(self):
        return self.nome


class Especialidade(models.Model):
    nome = models.CharField(max_length=100)  # Ex: Harmonização, Massoterapia, Depilação

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)  # Ex: Tratamento Facial, Corporal, Capilar

    def __str__(self):
        return self.nome


class Turno(models.Model):
    nome = models.CharField(max_length=50)  # Ex: Matutino, Vespertino

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, blank=True, null=True)
    componentes_alergicos = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.marca})"


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True) 
    data_nasc = models.DateField(blank=True, null=True) 
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True) 

    def __str__(self):
        return self.nome


class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True) 
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, blank=True) 
    especialidade = models.ForeignKey(Especialidade, on_delete=models.SET_NULL, null=True, blank=True) 
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    duracao_minutos = models.IntegerField(default=60) 
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True) 
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0.00) 

    def __str__(self):
        return self.nome



class TurnoTrabalho(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=50) 
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.profissional.nome} - {self.dia_semana} ({self.turno.nome})"



class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField(db_column='hora') 
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.cliente.nome} - {self.servico.nome} em {self.data}"


class FichaEvolucao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_atendimento = models.DateField()
    anotacoes_tecnicas = models.TextField()

    def __str__(self):
        return f"Evolução: {self.cliente.nome} - {self.data_atendimento}"


class AvaliacaoServico(models.Model):
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    nota = models.IntegerField() 
    comentario_cliente = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Nota {self.nota} para Agendamento {self.agendamento.id}"