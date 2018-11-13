from AvionCarga import AvionCarga
from AvionComercial import AvionComercial

class Hangar:

    def __init__(self):
        self.lista_avionesComerciales = []
        self.lista_avionesCarga = []
        self.cont_avionesCar = 0
        self.cont_avionesCom = 0
        archivo = open('Aviones.csv','r')
        for linea in archivo:
            partes = linea.split(',')
            #Obtiene los datos del avion
            id = partes[0]
            modelo = partes[1]
            estado = partes[2]
            tipo = partes[3]
            capacidad = partes[4]
            atributo = partes[5]
            if tipo == 'Comercial':
                avionComercial = AvionComercial(capacidad,atributo,id,modelo,estado)
                self.lista_avionesComerciales.append(avionComercial)
                self.cont_avionesCom += 1
            elif tipo == 'Carga':
                avionCarga = AvionCarga(capacidad,atributo,id,modelo,estado)
                self.lista_avionesCarga.append(avionCarga)
                self.cont_avionesCar += 1
        archivo.close()      
            


from Hangar import Hangar

h = Hangar()


