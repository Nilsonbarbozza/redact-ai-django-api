from django.db import models

class Artigo(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    categoria = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
