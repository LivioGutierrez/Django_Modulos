from django.db import models

class Vehiculo(models.Model):
    patente = models.CharField(max_length= 6, primary_key= True)
    marca = models.CharField(max_length= 20, null= False)
    modelo = models.CharField(max_length= 20, null= False)
    year = models.IntegerField(null= False)
    activo = models.BooleanField(default= False)

class Chofer(models.Model):
    rut = models.CharField(max_length= 9, primary_key= True)
    nombre = models.CharField(max_length= 50, null= False)
    apellido = models.CharField(max_length= 50, null= False)
    activo = models.BooleanField(default= False)
    creacion_registro = models.DateTimeField()
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.SET_NULL, null= True, unique= True)

class RegistroContabilidad(models.Model):
    fecha_compra = models.DateTimeField(null= False)
    valor = models.FloatField(null = False)
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.SET_NULL, null= True, unique= True)