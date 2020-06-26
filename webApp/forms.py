from django import forms
from .models import Funcionario

REGIAO = (
    ('AC','AC'),
    ('AL','AL'),
    ('AP','AP'),
    ('AM','AM'),
    ('BA','BA'),
    ('CE','CE'),
    ('DF','DF')

    )
US = (
    ('US','US Teste'),
    ('US','US Teste'),
    ('US','US Teste'),
    ('US','US Teste'),
    ('US','US Teste'),
    ('US','US Teste'),
    ('US','US Teste')
)

AGENCIA = (
    ('AG','AG Teste'),
    ('AG','AG Teste'),
    ('AG','AG Teste'),
    ('AG','AG Teste'),
    ('AG','AG Teste'),
    ('AG','AG Teste'),
    ('AG','AG Teste')
)
EQUIPES = (
    ('EQ','Equipe-01'),
    ('EQ','Equipe-02'),
    ('EQ','Equipe-03')
)

class FuncionarioForm(forms.ModelForm):
    nome = forms.CharField(
        label='Nome ',
        widget=forms.TextInput(attrs={'placeholder': 'Nome completo'}))
    cpf = forms.CharField(
        max_length=11,
        label='CPF ',
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: 123.456.789-10'}))
    email = forms.EmailField(
        label='E-mail ',
        widget=forms.TextInput(attrs={'placeholder': 'seuemail@mail.com'}))
    rg = forms.CharField(
        required= True,
        label='RG ',
        widget=forms.TextInput(attrs={'placeholder': '12.345.678'})
    )
    dt_nascimento = forms.DateField(
        label='Data Nascimento',
        required=True,
    )
    matricula_iki = forms.CharField(
        label='Matricula IKI ',
        widget=forms.TextInput(attrs={'placeholder': '12345'})
    )
    matricula_cemig = forms.CharField(
        label='Matricula CEMIG ',
        max_length=7,
        widget=forms.TextInput(attrs={'placeholder': 'E123456'})
    )
    regiao = forms.ChoiceField( choices=REGIAO
    )

    us = forms.ChoiceField(
        label='US ',
        choices=US,
    )
    agencia = forms.ChoiceField(
        label='Agencia ',
        choices=AGENCIA,
    )
    descricao = forms.CharField(
        label='Descrição ',
        widget=forms.Textarea,
        required = False
    )

    equipe = forms.ChoiceField(
        label='Equipe ',
        choices=EQUIPES
    )
    dt_admissao = forms.DateField(
        label='Data Admissão',
        required=True,
    )
    status = forms.BooleanField(
        label='Status'
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
