from django.db import models

# Create your models here

class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=15, default="", verbose_name="Nome ")
    apelido = models.CharField(max_length=15, default="", verbose_name="Apelido ")
    email = models.EmailField()
    telefone = models.CharField(max_length=17, blank=True)
    dataNascimento = models.DateField()
    dataCriacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=25, default="", verbose_name="Nome ")
    clareza = models.CharField(max_length=10, default=5)
    rigor = models.CharField(max_length=10, default=5)
    precisao = models.CharField(max_length=10, default=5)
    tempoResposta = models.BooleanField(verbose_name="Tempo de resposta do Website", default=False)
    facilUtilizacao = models.BooleanField(verbose_name="Fácil de utilizar", default=False)
    facilInterpretacao = models.BooleanField(verbose_name="Fácil de interpretar", default=False)
    Opiniao = models.TextField(default="")

    def __str__(self):
        return str(self.id)

class Quizz(models.Model):
    id = models.AutoField(primary_key=True)
    pontos = models.IntegerField(default=0)
    nome = models.CharField(max_length=30, default="", verbose_name="Nome ")
    p1 = models.CharField(max_length=30, default="")
    p2 = models.CharField(max_length=20, default="")
    p3 = models.CharField(max_length=40, default="")
    p4 = models.CharField(max_length=30, default="")
    p5 = models.CharField(max_length=40, default="")
    p6 = models.CharField(max_length=40, default="")
    p7 = models.CharField(max_length=40, default="")
    p8 = models.CharField(max_length=30, default="")
    p9 = models.CharField(max_length=30, default="")
    p10 = models.CharField(max_length=30, default="")

    def __str__(self):
        return str(self.id)


