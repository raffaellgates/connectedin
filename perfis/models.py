from django.db import models


class Perfis(models.Model):
    nome = models.CharField(max_length=128, blank=False)
    usuario = models.CharField(max_length=20, blank=False)
    contatos = models.ManyToManyField("self")

    def __str__(self):
        return self.nome


class User(models.Model):
    email = models.EmailField(max_length=25, blank=False)
    senha = models.CharField(max_length=20, blank=False)
    data_nascimento = models.DateField(blank=False)
    perfis = models.ManyToManyField(Perfis)

    def __str__(self):
        return self.email



class Reaction(models.Model):
    TIPOS_REACTION = [
    ('1', 'curtir'),
    ('2', 'amar'),
    ('3', 'rir'),
    ('4', 'imprecionar'),
    ('5', 'triste'),
    ('6', 'raiva')
]

    tipo_react = models.CharField(max_length=1 ,choices=TIPOS_REACTION)
    data = models.DateField(blank=False)
    perfil = models.ForeignKey(Perfis, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=4 ,decimal_places=0)

    def __str__(self):
        return self.tipo_react


class Comment(models.Model):
    texto = models.TextField(blank=False)
    data = models.DateField(blank=False)
    perfil = models.ForeignKey(Perfis, on_delete=models.CASCADE)

class Post(models.Model):
    texto = models.TextField(blank=False)
    date_post = models.DateField(blank=False)
    perfil = models.ForeignKey(Perfis, on_delete=models.CASCADE)
    comentarios = models.ManyToManyField(Comment)
    reaction = models.ManyToManyField(Reaction)


class TimeLine(models.Model):
    postagens = models.ManyToManyField(Post)
    perfil = models.ForeignKey(Perfis, on_delete=models.CASCADE)




