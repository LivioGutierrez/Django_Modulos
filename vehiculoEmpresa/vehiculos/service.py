from .models import Vehiculo, Chofer, RegistroContabilidad

def crear_vehiculo(pPatente, pMarca, pModelo, pYear, pActivo= False):
    vehiculo = Vehiculo(patente= pPatente, marca = pMarca, modelo = pModelo, year = pYear, activo= pActivo)
    vehiculo.save()

def crear_chofer(pRut, pNombre, pApellido, pActivo, pCreacion_registro):
    chofer = Chofer(rut = pRut, nombre = pNombre, apellido = pApellido, activo = pActivo, creacion_registro = pCreacion_registro)
    chofer.save()

def crear_registro_contable(pFecha_compra, pValor):
    registro_contable = crear_registro_contable(fecha_compra = pFecha_compra, pValor = pValor)
    registro_contable.save()

def deshabilitar_chofer():
    pass

def deshabilitar_vehiculo():
    pass

def habilitar_chofer():
    pass

def habilitar_vehiculo():
    pass

def obtener_vehiculo():
    pass

def obtener_chofer():
    pass

def asignar_chofer_a_vehiculo():
    pass

def imprimir_datos_vehiculos():
    pass
