# Generated by Django 3.0.7 on 2020-06-25 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0002_auto_20200625_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treinamento',
            name='titulo',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
