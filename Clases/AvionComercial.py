from Avion import Avion
from Vuelo import Vuelo
class AvionComercial(Avion):

    def __init__(self,capacidad,clase,id,modelo,estado):
        Avion.__init__(self,id,modelo,estado)
        self.capacidad = capacidad
        self.clase = clase
        self.setVuelos()
    
    def imprimir(self):
        print('--------------------------')
        print('ID Avion:', self._id)
        print('Modelo: ',self._modelo)
        print('Estado: ',self._estado)
        print('Clase: ',self.clase)
        print('Capacidad de pasajeros: ',self.capacidad)
    
    def setVuelos(self):
        archivo = open('VuelosComerciales.csv','r')
        for linea in archivo:
            partes = linea.split(',')
            idAvion = int(partes[0])
            if(idAvion == self._id):
                idVuelo = partes[1]
                hora_llegada = partes[2]
                hora_salida = partes[3]
                ciudad = partes[4]
                v = Vuelo(idVuelo,hora_llegada,hora_salida,ciudad)
                self._vuelos.append(v)
        archivo.close()
