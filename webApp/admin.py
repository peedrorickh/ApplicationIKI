from django.contrib import admin
from .models import Funcionario, Controle, DadosBancarios,Treinamento, Prova
# Register your models here.


admin.site.register(Funcionario)
admin.site.register(Controle)
admin.site.register(DadosBancarios)
admin.site.register(Treinamento)
admin.site.register(Prova)



admin.site.site_header = 'Administração'
admin.site.site_title = 'Administração'