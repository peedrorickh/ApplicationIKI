from django.contrib import admin
from .models import Funcionario, US, Cargo, Treinamento, Provas
# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Cargo)
admin.site.register(Treinamento)
admin.site.register(US)
admin.site.register(Provas)



admin.site.site_header = 'Administração'
admin.site.site_title = 'Administração'