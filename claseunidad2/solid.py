#solid principles 
# 1. single responsibility principle una clase tiene una unica responsabilidad del modulo en el que hace parte

#no aplicado: 

class Report: 
    def __init__(self, data ):
        self.data = data
    def calcular_estads(self):
        pass    
    def guardar_archivo(self, tipoarchivo):
        if tipoarchivo == "EXCEL":
            print ("Generando reporte en PDF")
        elif tipoarchivo == "PDF":
            print ("Generando reporte en PDF")
        else: 
            print ("formato no soportado")
            
    def notificarcambios(self):
        print (f"hubo un cambio en los datos: {self.data}")
        
#¿Cual es la solucion separando responsabilidades con 3 clases?

class Report:
    def __init__(self, data):
        self.data = data

    def calcular_estads(self):
        pass

class ReportSaver:
    def guardar_archivo(self, data, tipoarchivo):
        if tipoarchivo == "EXCEL":
            print("Generando reporte en EXCEL")
        elif tipoarchivo == "PDF":
            print("Generando reporte en PDF")
        else:
            print("formato no soportado")

class ReportNotifier:
    def notificar_cambios(self, data):
        print(f"Hubo un cambio en los datos: {data}")

#2. open/closed principle las clases deben estar abiertas para extension pero cerradas para modificacion
#no aplicado:

class Descuento:
    def __init__(self, tipo_cliente):
        self.tipo_cliente = tipo_cliente

    def aplicar_descuento(self, precio):
        if self.tipo_cliente == "regular":
            print("descuento para cliente regular aplicado")
        elif self.tipo_cliente == "premium":
            print("descuento para cliente premium aplicado")
            
    #que pasa si se quiere agregar un descuento para un nuevo tipo de cliente? 
#separar en funciones de la misma clase o en clases distintas

#Liskov Subtitution Principle: 
#en un modulo de software donde se implemente generalizacion a travez de herencia deberia poder usarse la subclase en reemplazo de la super clase y viceversa

class Ave:
    
    def __init__(self):
        pass
    def volar():
        print("El ave está volando")
        
class avestruz(Ave):
    def volar():
        raise Exception("No puede volar")
    
#Solucion: generalizar mas 
class ave:
    #no implementa metodos que las aves no voladoras no expongan
    pass
class avevoladora(ave):
    def __init__(self):
        pass
    
    def volar():
        print("El ave está volando")
    