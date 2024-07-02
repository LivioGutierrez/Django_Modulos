from django.db import models

class Profesor(models.Model):
    rut = models.CharField(max_length = 9, null = False, primary_key=True)
    nombre = models.CharField(max_length = 50, null = False)
    apellido = models.CharField(max_length = 50, null = False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateTimeField()
    modificacion_registro = models.DateTimeField()
    creado_por = models.CharField(max_length = 50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Curso(models.Model):
    codigo = models.CharField(max_length=10, null=False, unique=True)
    nombre = models.CharField(max_length = 50, null = False)
    version = models.IntegerField()
    # profesor_id = models.CharField(max_length=9, unique=True) creo que con esto estaria relacionada

class Estudiante(models.Model):
    rut = models.CharField(max_length= 9, null=False)
    nombre = models.CharField(max_length = 50, null = False)
    apellido = models.CharField(max_length = 50, null = False)
    fecha_nac = models.DateTimeField(null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateTimeField()
    modificacion_registro = models.DateTimeField()
    creado_por = models.CharField(max_length=50, null=True, blank=True)

class Direccion(models.Model):
    pass