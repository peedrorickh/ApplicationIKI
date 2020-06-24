from django.contrib import admin
from .models import Usuario, Cargo, Treinamento, Post
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Cargo)
admin.site.register(Treinamento)
admin.site.register(Post)


admin.site.site_header = 'Administração'
admin.site.site_title = 'Administração'