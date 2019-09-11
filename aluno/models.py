from django.db import models

from professor.models import Professor


class Aluno(models.Model):
    object = None
    objects = None
    nome = models.CharField(
        max_length=255,
        verbose_name='Nome',
    )

    idade = models.IntegerField(
        verbose_name='Idade',
    )

    email = models.EmailField(
        max_length=255,
        verbose_name='Email',
    )
    prof_favorito = models.ForeignKey(
        Professor,
        on_delete= models.CASCADE,
        related_name= 'alunos'
    )

    def __str__(self):
        return self.nome