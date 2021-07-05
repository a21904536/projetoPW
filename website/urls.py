
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name=' '),
    path('home', views.home_page_view, name='home'),
    path('recordes', views.recordes, name='recordes'),
    path('equipas', views.equipas, name='equipas'),
    path('epoca', views.epoca, name='epoca'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('contacto', views.contacto_page_view, name="contacto"),
    path('about', views.about, name='about'),
    path('comentario', views.comentarios_page_view, name='comentario'),
]