from Avion import Avion
from Vuelo import Vuelo
class AvionCarga(Avion):

    def __init__(self,capacidad,volumen,id,modelo,estado, capacidadactual, precio_carga):
        Avion.__init__(self,id,modelo,estado)
        self.capacidad = capacidad
        self.volumen = volumen
        self.capacidadactual = capacidadactual
        self.precio_carga = precio_carga
        self.setVuelos()
        self.setPrecios()

    
    def imprimir(self):
        print('--------------------------')
        print('ID Avion:', self._id)
        print('Modelo: ',self._modelo)
        print('Estado: ',self._estado)
        print('Volumen',self.volumen)
        print('Capacidad de carga: ',self.capacidad)
        print('Capacidad actual: ',self.capacidadactual)
        print('Precio por kilo: ', self.precio_carga)

    def setVuelos(self):
        archivo = open('VuelosCarga.csv','r')
        for linea in archivo:
            partes = linea.split(',')
            idAvion = int(partes[0])
            if(idAvion == self._id):
                idVuelo = partes[1]
                hora_llegada = partes[2]
                hora_salida = partes[3]
                ciudad = partes[4]
                capacidadactual = partes[5]
                v = Vuelo(idVuelo,hora_llegada,hora_salida, ciudad, capacidadactual)
                self._vuelos.append(v)
        archivo.close()
    
    def setPrecios(self):
        archivo2 = open('Precios.csv', 'r')
        for linea in archivo2:
            partes = linea.split(',')
            precio_carga = partes[8]
        archivo2.close() 