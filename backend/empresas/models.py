from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

cnpj_validator = RegexValidator(
    r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$',
    'CNPJ inválido. Formato correto: 00.000.000/0000-00'
)

class Empresa(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=55)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.nome

# Create your models here.
