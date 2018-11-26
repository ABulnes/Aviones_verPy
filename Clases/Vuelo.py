from Boleto import Boleto
from Archivo import Archivo
class Vuelo:

    def __init__(self,id,hora_llegada,hora_salida,ciudad,capacidadactual = 0):
        self._id = id
        self._hora_llegada = hora_llegada
        self._hora_salida = hora_salida
        self._ciudad = ciudad
        self.num_pasajeros = 0
        self._pasajeros = []
        self.initBoletos(self._id)
        self.capacidadactual = capacidadactual

    def imprimir(self):
        print('--------------------')
        print('ID Vuelo: ',self._id)
        print('Hora de llegada: ',self._hora_llegada)
        print('Hora de salida: ',self._hora_salida)
        print('Ciudad de Destino: ', self._ciudad)
        print('Capacidad Actual: ', self.capacidadactual)
    
    def initBoletos(self,id):
        try:
            archivo = open('Boletos.csv','r')
            for linea in archivo:
                partes = linea.split(',')
                idVuelo = partes[0]
                if(idVuelo == self._id):
                    nombre = partes[1]
                    asiento = partes[2]
                    b = Boleto(nombre,asiento)
                    self._pasajeros.append(b)
                    self.num_pasajeros += 1
            archivo.close()
        except:
             print('Ocurrio un error al abrir el archivo')
    
    #Agrega el pasajero al archivo Boletos.csv
    def addPasajero(self,nombre,asiento):
        try:
            archivo = open('Boletos.csv','a')
            linea = ','.join([self._id,nombre,asiento])
            archivo.write(linea)
            archivo.close
            return True
        except:
            print('Ocurrio un error al abrir el archivo')

    #Reserva boletos en la lista
    def reservar(self,nombre,asiento):
        if(self.addPasajero(nombre,asiento)):
            b = Boleto(nombre,asiento)
            self._pasajeros.append(b)
            self.num_pasajeros +=1

    def delPasajero(self,nombre):
        try:
            op_ar = Archivo()
            op_ar.eliminar('Boletos.csv',nombre)
            return True
        except:
            print('Ocurrio un error al eliminar el pasajero')
            return False

    def eliminarPasajero(self,nombre):
        if(self.delPasajero(nombre)):
            if nombre in self._pasajeros:
                self._pasajeros.remove(nombre)
                self.num_pasajeros -= 1
                return True