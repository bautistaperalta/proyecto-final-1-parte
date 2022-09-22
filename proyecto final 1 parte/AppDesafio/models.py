from django.db import models

class Datos_personales(models.Model):
    usuario = models.EmailField()
    contraseña = models.IntegerField()
    def __str__(self):
        return self.usuario

class Datos_registro(models.Model):
    nombre_completo = models.CharField(max_length=40)
    email = models.EmailField()
    fechaDeNacimiento = models.DateField()
    contraseña = models.IntegerField()

class Datos_experiencia(models.Model):
    empleador = models.CharField(max_length=40)
    puesto= models.CharField(max_length=40)
    fechaDeinicio = models.DateField()
    fechaDefin= models.DateField()

class Datos_hobbies(models.Model):
    hobbie = models.CharField(max_length=40)
    

    