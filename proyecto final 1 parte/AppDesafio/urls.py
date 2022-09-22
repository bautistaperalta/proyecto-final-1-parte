from django.urls import path
from AppDesafio.views import *
urlpatterns = [
    
   
    path('buscar_user/', buscar_user),
    path('registro/', registro),
    path('experiencia/', experiencia),
    path('hobbie/', hobbie),
  
]