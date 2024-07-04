from django.db import models

class Curso(models.Model):
    codigo = models.CharField(max_length=10, null=False, unique=True, primary_key=True)
    nombre = models.CharField(max_length = 50, null = False)
    version = models.IntegerField()
    
class Profesor(models.Model):
    rut = models.CharField(max_length = 9, null = False, primary_key=True)
    nombre = models.CharField(max_length = 50, null = False, blank=False)
    apellido = models.CharField(max_length = 50, null = False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateTimeField()
    modificacion_registro = models.DateTimeField()
    creado_por = models.CharField(max_length = 50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cursos = models.ManyToManyField(Curso, related_name='Profesores')
    
class Estudiante(models.Model):
    rut = models.CharField(max_length= 9, null=False, blank=False, primary_key=True)
    nombre = models.CharField(max_length = 50, null = False, blank=False)
    apellido = models.CharField(max_length = 50, null = False, blank=False)
    fecha_nac = models.DateTimeField(null=False, blank=False)
    activo = models.BooleanField(default=False, blank=False)
    creacion_registro = models.DateTimeField()
    modificacion_registro = models.DateTimeField()
    creado_por = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    curso = models.ForeignKey(Curso, related_name='estudiantes', on_delete=models.CASCADE )

class Direccion(models.Model):
    calle = models.CharField(max_length = 50, null=False) 
    numero = models.IntegerField(null=False) # me pide quitar el max_length=10,
    dpto = models.CharField(max_length=10, default="")
    comuna = models.CharField(max_length=50, null=False)
    ciudad = models.CharField(max_length=50, null= False)
    region = models.CharField(max_length=50, null= False)
    estudiante = models.OneToOneField(Estudiante, related_name='direcciones', on_delete=models.CASCADE)