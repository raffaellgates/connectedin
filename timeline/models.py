from django.db import models
from perfis.models import Perfil

class Publicacao(models.Model):
    publicacao = models.TextField()
    usuario = models.ForeignKey(Perfil,on_delete=models.CASCADE,related_name='perfis_pub')
    data_publicacao = models.DateTimeField(auto_now=True)

def test():
    pass
