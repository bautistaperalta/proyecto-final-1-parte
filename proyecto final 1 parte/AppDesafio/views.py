from django.shortcuts import render
from django.http import HttpResponse
from AppDesafio.models import Datos_registro, Datos_experiencia, Datos_hobbies

# Create your views here.

#def registro(request):
    #if request.method == "POST":
    #    estudiante = Datos_registro(nombre_completo = request.POST['nombre_completo'], fechaDeNacimiento = request.POST['fechaDeNacimiento'], email = request.POST['email'], contraseña = request.POST['contraseña'])
   #     estudiante.save()
  #      return render(request, "home.html")
 #   return render(request, "registro.html")
def buscar_user(request):
    if request.GET["email"]:
        email = request.GET["email"]
        usuarios = Datos_registro.objects.filter(email__icontains = email) 
        return render(request, "registro.html", {"usuarios": usuarios})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)
def registro(request):
    if request.method == "POST":
        estudiante = Datos_registro(nombre_completo = request.POST['nombre_completo'], fechaDeNacimiento = request.POST['fechaDeNacimiento'], email = request.POST['email'], contraseña = request.POST['contraseña'])
        estudiante.save()
        return render(request, "home.html")
    return render(request, "registro.html")
def experiencia(request):
    if request.method == "POST":
        experiencia = Datos_experiencia(empleador = request.POST['empleador'],puesto = request.POST['puesto'], fechaDeinicio = request.POST['fechaDeinicio'], fechaDefin = request.POST['fechaDefin'])
        experiencia.save()
        return render(request, "home.html")
    return render(request, "experiencia.html")
def hobbie(request):
    if request.method == "POST":
        hobbie = Datos_hobbies(hobbie = request.POST['hobbie'])
        hobbie.save()
        return render(request, "home.html")
    return render(request, "hobbie.html")