from django.db import models

# Create your models here.
class  dados_usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length= 255 ,null=False)
    email = models.TextField(max_length= 255 ,null=False)
    idade = models.IntegerField(null=False)
