# Generated by Django 3.0.7 on 2020-07-03 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Controle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcionario', models.CharField(max_length=50)),
                ('matricula', models.CharField(max_length=7)),
                ('pis', models.CharField(max_length=15)),
                ('dias_semana', models.IntegerField()),
                ('dias_pagar', models.IntegerField()),
                ('vale_transporte', models.BooleanField()),
                ('opcao', models.CharField(max_length=25)),
                ('tarifa_ida', models.DecimalField(decimal_places=2, max_digits=3)),
                ('tarifa_volta', models.DecimalField(decimal_places=2, max_digits=3)),
                ('total_dia', models.IntegerField()),
                ('saldo_mes', models.DecimalField(decimal_places=2, max_digits=3)),
                ('recarregar', models.BooleanField()),
                ('doc_pendente', models.BooleanField()),
                ('folha_ponto', models.BooleanField()),
                ('ferias_inicio', models.DateField()),
                ('termino_ferias', models.DateField()),
                ('ASO_periodico', models.CharField(choices=[('', ''), ('S', 'Sim'), ('S', 'Não')], max_length=1)),
                ('plano_saude', models.CharField(choices=[('', ''), ('S', 'Sim'), ('S', 'Não')], max_length=1)),
                ('plano_odonto', models.CharField(choices=[('', ''), ('S', 'Sim'), ('S', 'Não')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.CharField(max_length=10)),
                ('dt_nascimento', models.DateField()),
                ('matricula_iki', models.CharField(max_length=5)),
                ('matricula_cemig', models.CharField(max_length=7, unique=True)),
                ('regiao', models.CharField(max_length=30)),
                ('us', models.CharField(max_length=30)),
                ('agencia', models.CharField(max_length=30)),
                ('descricao', models.TextField(max_length=40)),
                ('equipe', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=254)),
                ('dt_admissao', models.DateField()),
                ('funcao', models.CharField(max_length=15)),
                ('status', models.CharField(choices=[('', ''), ('ON', 'Ativo'), ('AW', 'Afastado'), ('VAC', 'Férias'), ('OFF', 'Desligado')], max_length=3)),
            ],
            options={
                'verbose_name_plural': 'funcionario',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Treinamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=25, null=True, unique=True)),
                ('resumo', djrichtextfield.models.RichTextField(max_length=20)),
                ('dt_publicacao', models.DateField(auto_now=True)),
                ('publicacao', djrichtextfield.models.RichTextField()),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField()),
                ('aluno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webApp.Funcionario')),
                ('titulo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webApp.Treinamento')),
            ],
        ),
    ]
