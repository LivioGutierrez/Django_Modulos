from .models import Vehiculo, Chofer, RegistroContabilidad

def crear_vehiculo(pPatente, pMarca, pModelo, pYear, pActivo= False):
    vehiculo = Vehiculo(patente= pPatente, marca = pMarca, modelo = pModelo, year = pYear, activo= pActivo)
    vehiculo.save()

def crear_chofer(pRut, pNombre, pApellido, pActivo, pCreacion_registro):
    chofer = Chofer(rut = pRut, nombre = pNombre, apellido = pApellido, activo = pActivo, creacion_registro = pCreacion_registro)
    chofer.save()

def crear_registro_contable(pFecha_compra, pValor):
    registro_contable = RegistroContabilidad(fecha_compra = pFecha_compra, pValor = pValor)
    registro_contable.save()

def deshabilitar_chofer(rut_chofer, activo = False):
    obj_chofer = Chofer.objects.get(pk= rut_chofer)
    
    deshabilitarChofer = Chofer(obj_chofer, activo = activo)
    deshabilitarChofer.save()

def deshabilitar_vehiculo(patante_vehiculo, activo = False):
    obj_vehiculo = Vehiculo.objects.get(pk = patante_vehiculo)
    
    deshabilitarVehiculo = Vehiculo(obj_vehiculo, activo = activo)
    deshabilitarVehiculo.save()

def habilitar_chofer(rut_chofer, activo = True):
    obj_chofer = Chofer.objects.get(pk= rut_chofer)
    
    deshabilitarChofer = Chofer(obj_chofer, activo = activo)
    deshabilitarChofer.save()

def habilitar_vehiculo(patante_vehiculo, activo = True):
    obj_vehiculo = Vehiculo.objects.get(pk = patante_vehiculo)
    
    deshabilitarVehiculo = Vehiculo(obj_vehiculo, activo = activo)
    deshabilitarVehiculo.save()

def obtener_vehiculo():
    lista_vehiculo = Vehiculo.objects.all()# Cambiar, creo que aca solo va esta linea y en la funcion " imprimir_datos_vehiculos" va el for
    for lista in lista_vehiculo:
        print(f"Patente: {lista.patente}\n 
                Marca: {lista.marca}\n 
                Modelo: {lista.modelo}\n 
                Año: {lista.year}\n 
                Activo: { lista.activo}")

def obtener_chofer():
    lista_chofer = Chofer.objects.all()
    for lista in lista_chofer:
        print(f"Rut: {lista.rut}\n 
            Nombre: {lista.nombre}\n 
            Apellido: {lista.apellido}\n 
            Fecha de registro: {lista.creacion_registro}\n 
            Vehiculo: {lista.vehiculo}\n 
            Activo: {lista.activo}")
    pass

def asignar_chofer_a_vehiculo():
    pass

def imprimir_datos_vehiculos():
    pass
