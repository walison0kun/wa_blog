from django.db import models

# Create your models here.
class author(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    idade = models.IntegerField(max_length=2)
    sexo = models.TextField(max_length=10, null=False)
    e_mail = models.EmailField(max_length=254, null=False)
    resu_perfil = models.CharField(max_length=255)