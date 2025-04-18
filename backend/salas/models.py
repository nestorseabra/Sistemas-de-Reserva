
from django.db import models
from django.conf import settings
from .models import Sala  
from django.utils import timezone


class Reserva(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovada', 'Aprovada'),
        ('rejeitada', 'Rejeitada'),
    ]

    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reservas'
    )
    sala = models.ForeignKey(
        Sala,
        on_delete=models.CASCADE,
        related_name='reservas'
    )
    data_hora = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pendente'
    )
    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES,
        default='media'
    )

    def __str__(self):
        return f"Reserva de {self.user.username} para {self.sala.nome} em {self.data_hora}"
# Create your models here.
