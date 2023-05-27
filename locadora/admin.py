from django.contrib import admin
from .models import Categoria, Cliente, Locacao, Filme
# Register your models here.

@admin.register(Categoria)
class categoriaAdmin(admin.ModelAdmin):
    list_display = ('nome_cat',)

@admin.register(Cliente)
class clienteAdmin(admin.ModelAdmin):
    list_display = ('nome_cli', 'email')

@admin.register(Locacao)
class locacaoAdmin(admin.ModelAdmin):
    list_display = ('nome_loc', 'data', 'cliente')

@admin.register(Filme)
class filmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'valor', 'filme_cat')
