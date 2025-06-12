from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.nome

class Certificado(models.Model):
    nome = models.CharField(max_length=200)
    link = models.URLField()
    credencial = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Mensagem(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.email}'
