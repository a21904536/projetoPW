from django.shortcuts import render
from .forms import ContactoForm, ComentarioForm, QuizzForm
from .models import Contacto
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.urls import reverse

def home_page_view(request):
	return render(request, 'website/home.html')

def epoca(request):
    return render(request, 'website/epoca.html')

def recordes(request):
    return render(request, 'website/recordes.html')

def equipas(request):
    return render(request, 'website/equipas.html')

def about(request):
    return render(request, 'website/about.html')

def contacto_page_view(request):
    form = ContactoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:home'))

    context = {'form': form}

    return render(request, 'website/contacto.html', context)

def quizz_page_view(request):
    form = QuizzForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:quizz'))

    context = {
        'form': form,
    }
    return render(request, 'website/quizz.html', context)

def comentarios_page_view(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()



    context = {'form': form}

    return render(request, 'website/comentario.html', context)