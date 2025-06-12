from django.contrib.auth.hashers import make_password, check_password
from django.db import models

OBJETIVO_CHOICES = [
    ('hipertrofia', 'Hipertrofia'),
    ('emagrecimento', 'Emagrecimento'),
    ('definicao', 'Definição'),
]

NIVEL_CHOICES = [
    ('sedentário','Sedentário'),
    ('leve', 'Leve'),
    ('moderado', 'Moderado'),
    ('intenso', 'Intenso'),
    ('atleta', 'Atleta')
]

ALIMENTACAO_CHOICES = [
    ('vegano','Vegano'),
    ('vegetariano', 'Vegetariano'),
    ('sem gluten', 'Sem Gluten'),
    ('sem lactose', 'Sem Lactose'),
    ('sem restrições', 'Sem Restrições')
]

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    idade = models.PositiveIntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    objetivo = models.CharField(max_length=20, choices=OBJETIVO_CHOICES)
    nivelatv = models.CharField(max_length=20, choices=NIVEL_CHOICES)
    alimentacao = models.CharField(max_length=20, choices=ALIMENTACAO_CHOICES)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nome}"
