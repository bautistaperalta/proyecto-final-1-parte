from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppDesafio.models import Datos_registro, Datos_personales
from django.contrib import admin

def home(request):
    return render (request, 'home.html')

def experiencia(request):
    return render (request, 'experiencia.html')

def registro(request):
    return render(request, "registro.html")
