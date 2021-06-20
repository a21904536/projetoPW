from django.forms import ModelForm
from django import forms
from .models import Contacto, Comentario, Quizz

class ContactoForm(ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'



class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        opcoes = [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5)
        ]
        widgets = {
            'clareza': forms.RadioSelect(choices=opcoes),
            'rigor': forms.RadioSelect(choices=opcoes),
            'precisao': forms.RadioSelect(choices=opcoes),
        }

class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'
        labels = {
            'p1': "De que cor é o logótipo óficial da Formula 1? ",
            'p2': "Qual é a data do último GP no calendário da Formula 1? ",
            'p3': "Quantas equipas existem na época 2021 da Fórmula 1? ",
            'p4': "Qual foi o piloto que ganhou o Grande Prémio de Portugal 2021? ",
            'p5': "Qual o ano em que Lewis Hamilton ganhou o primeiro título? ",
            'p6': "Qual a equipa com mais títulos de construtores? ",
            'p7': "Em que ano Michael Schumacher atingiu a sua última vitória? ",
            'p8': "Quantos títulos conquistou Ayrton Senna? ",
            'p9': "De que equipa é o piloto George Russell? ",
            'p10': "Gosta de Formula 1? ",
        }