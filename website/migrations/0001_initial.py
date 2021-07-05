# Generated by Django 3.2.5 on 2021-07-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(default='', max_length=25, verbose_name='Nome ')),
                ('clareza', models.CharField(default=5, max_length=10)),
                ('rigor', models.CharField(default=5, max_length=10)),
                ('precisao', models.CharField(default=5, max_length=10)),
                ('tempoResposta', models.BooleanField(default=False, verbose_name='Tempo de resposta do Website')),
                ('facilUtilizacao', models.BooleanField(default=False, verbose_name='Fácil de utilizar')),
                ('facilInterpretacao', models.BooleanField(default=False, verbose_name='Fácil de interpretar')),
                ('Opiniao', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(default='', max_length=15, verbose_name='Nome ')),
                ('apelido', models.CharField(default='', max_length=15, verbose_name='Apelido ')),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=17)),
                ('dataNascimento', models.DateField()),
                ('dataCriacao', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pontos', models.IntegerField(default=0)),
                ('nome', models.CharField(default='', max_length=30, verbose_name='Nome ')),
                ('p1', models.CharField(default='', max_length=30)),
                ('p2', models.CharField(default='', max_length=20)),
                ('p3', models.CharField(default='', max_length=40)),
                ('p4', models.CharField(default='', max_length=30)),
                ('p5', models.CharField(default='', max_length=40)),
                ('p6', models.CharField(default='', max_length=40)),
                ('p7', models.CharField(default='', max_length=40)),
                ('p8', models.CharField(default='', max_length=30)),
                ('p9', models.CharField(default='', max_length=30)),
                ('p10', models.CharField(default='', max_length=30)),
            ],
        ),
    ]