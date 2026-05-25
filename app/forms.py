from django import forms
from .models import Cliente, Profissional, Servico, Agendamento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  # Puxa todos os campos da tabela automaticamente

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = '__all__'

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }