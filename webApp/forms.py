from crispy_forms.layout import Submit
from django import forms
from .models import Funcionario
from crispy_forms.helper import FormHelper


REGIAO = (
    ('', ''),
    ('CENTRO', 'CENTRO'),
    ('LESTE', 'LESTE'),
    ('MANTIQUEIRA', 'MANTIQUEIRA'),
    ('NORTE', 'NORTE'),
    ('OESTE', 'OESTE'),
    ('SUL', 'SUL'),
    ('SUPORTE', 'SUPORTE'),
    ('TRIÂNGULO', 'TRIÂNGULO')

)
US = (
    ('', ''),
    ('US', 'US Teste'),
    ('US', 'US Teste'),
    ('US', 'US Teste'),
    ('US', 'US Teste'),
    ('US', 'US Teste'),
    ('US', 'US Teste'),
    ('US', 'US Teste')
)

AGENCIA = (
    ('', ''),
    ('Teste1', 'AG Teste'),
    ('Teste2', 'AG Teste'),
    ('Teste3', 'AG Teste'),
    ('Teste4', 'AG Teste'),
    ('Teste5', 'AG Teste'),
    ('Teste6', 'AG Teste'),
    ('Teste7', 'AG Teste')
)
EQUIPES = (
    ('', ''),
    ('EQ1', 'Equipe-01'),
    ('EQ2', 'Equipe-02'),
    ('EQ3', 'Equipe-03')
)

FUNCAO = (
    ('', ''),
    ('Administrador', 'Administrador'),
    ('EQ2', '-02'),
    ('EQ3', '-03')
)



class DateInput(forms.DateInput):
    input_type = 'date'


class FuncionarioForm(forms.ModelForm):
    nome = forms.CharField(
        label='Nome ',
        widget=forms.TextInput(attrs={'placeholder': 'Nome completo'})
    )
    cpf = forms.CharField(max_length=11,
                          label='CPF ',
                          widget=forms.TextInput(attrs={'placeholder': 'Ex.: 123.456.789-10'})
                          )
    email = forms.EmailField(label='E-mail ',
                             widget=forms.TextInput(attrs={'placeholder': 'seuemail@mail.com'})
                             )
    rg = forms.CharField(required=True,
                         label='RG ',
                         widget=forms.TextInput(attrs={'placeholder': '12.345.678'})
                         )
    dt_nascimento = forms.DateField(label='Data Nascimento',
                                    required=True,
                                    widget=forms.DateInput(format='%d/%m/%Y')
                                    )
    matricula_iki = forms.CharField(label='Matricula IKI ',
                                    widget=forms.TextInput(attrs={'placeholder': '12345'})
                                    )
    matricula_cemig = forms.CharField(label='Matricula CEMIG ',
                                      max_length=7,
                                      widget=forms.TextInput(attrs={'placeholder': 'E123456'})
                                      )
    regiao = forms.ChoiceField(choices=REGIAO
                               )
    us = forms.ChoiceField(label='US ',
                           choices=US,
                           )
    agencia = forms.ChoiceField(label='Agencia ',
                                choices=AGENCIA,
                                )
    descricao = forms.CharField(label='Descrição ',
                                widget=forms.Textarea,
                                required=False
                                )

    equipe = forms.ChoiceField(label='Equipe ',
                               choices=EQUIPES
                               )
    dt_admissao = forms.DateField(label='Data Admissão',
                                  required=True,
                                  )
    status = forms.ChoiceField(label='Status',
                               choices = Funcionario.STATUS,
                               required=True,
                                )
    funcao = forms.ChoiceField(label='Função ',
                               choices=FUNCAO
                               )

    class Meta:
        model = Funcionario

        fields = [
            'nome',
            'cpf',
            'rg',
            'dt_nascimento',
            'matricula_iki',
            'matricula_cemig',
            'regiao',
            'us',
            'agencia',
            'descricao',
            'equipe',
            'email',
            'dt_admissao',
            'funcao',
            'status'
        ]
