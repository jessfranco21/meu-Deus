from django.db import models

# Create your models here.
class Aluno(models.Model):

    nome = models.CharField(
        max_length=255,
        verbose_name='Nome',
    )

    idade = models.CharField(
        max_length=5,
        verbose_name='Idade',
    )

    email = models.EmailField(
        max_length=50,
        verbose_name='Email',
    )

    def __str__(self):
        return self.nome.title()