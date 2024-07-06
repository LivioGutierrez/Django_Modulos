from .models import Curso, Profesor, Estudiante, Direccion

def crear_curso(pCodigo, pNombre, pVersion= None):
    curso = Curso(codigo=pCodigo, nombre=pNombre, version=pVersion)
    curso.save()
    return curso

def crear_profesor(pRut, pNombre, pApellido, pCreado_por, pActivo = False):
    profesor = Profesor(rut=pRut, nombre= pNombre, apellido= pApellido, creado_por= pCreado_por, activo= pActivo)
    profesor.save()
    return profesor

def crear_estudiante(pRut, pNombre, pApellido, pFecha_nac, pCreado_por, pActivo=False):
    estudiante = Estudiante(rut=pRut, nombre= pNombre, apellido= pApellido, fecha_nac=pFecha_nac, creado_por= pCreado_por, activo= pActivo)
    estudiante.save()
    return estudiante

def crear_direccion(rut_estudiante, pCalle, pNumero,  pComuna, pCiudad, pRegion, pDpto=None):
    obj_estudiante = Estudiante.objects.get(pk=rut_estudiante)
    
    direccion = Direccion(estudiante = obj_estudiante, calle=pCalle, numero=pNumero, dpto=pDpto, comuna=pComuna, ciudad=pCiudad, region=pRegion)
    direccion.save()
    return direccion

def obtiene_estudiante(rut):
    return Estudiante.objects.get(pk=rut)

def obtiene_profesor(rut):
    return Profesor.objects.get(pk=rut)

def obtiene_curso(codigo):
    return Curso.objects.get(pk=codigo)

def agrega_profesor_a_curso(rut, codigo):
    profesor = obtiene_profesor(rut)
    curso = obtiene_curso(codigo)
    
    profesor.cursos.add(curso)

def agrega_cursos_a_estudiante(rut, codigo):
    estudiante = obtiene_estudiante(rut)
    curso = obtiene_curso(codigo)
    
    estudiante.curso.add(curso)

def imprime_estudiante_cursos():
    lista_cursos = Curso.objects.all()
    
    for curso in lista_cursos:
        print("curso", curso)

        lista_profesores = curso.profesores.all()
        for profesor in lista_profesores:
            print(profesor)
            
        lista_estudiante = curso.estudiantes.all()
        for estudiante in lista_estudiante:
            print(estudiante)