from django.db import models

class Funcionario(models.Model):
    CARGOS = [
        ('assistente', 'Assistente'),
        ('analista', 'Analista'),
        ('coordenador', 'Coordenador'),
    ]
    
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)  # Idealmente, use autenticação Django em vez de armazenar senhas diretamente
    cargo = models.CharField(max_length=20, choices=CARGOS)
    chave = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome
