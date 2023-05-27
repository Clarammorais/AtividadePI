from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome_cat = models.CharField(max_length=150)
    
    def __str__(self):
        return f'{self.nome_cat}'

class Cliente(models.Model):
    nome_cli = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return f'{self.nome_cli}'

class Locacao(models.Model):
    nome_loc = models.CharField(max_length=150)
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome_loc}'

class Filme(models.Model):
    titulo = models.CharField(max_length=150)
    valor = models.IntegerField()
    filme_cat = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    locacao = models.ManyToManyField(Locacao) 

    def __str__(self):
        return f'{self.filme_cat}'


    