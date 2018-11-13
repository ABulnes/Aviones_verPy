from Boleto import Boleto

class Vuelo:

    def __init__(self,id,hora_llegada,hora_salida,ciudad):
        self._id = id
        self._hora_llegada = hora_llegada
        self._hora_salida = hora_salida
        self._ciudad = ciudad
        self.num_pasajeros = 0
        self._pasajeros = []
        self.initBoletos(self._id)

    def imprimir(self):
        print('--------------------')
        print('ID Vuelo: ',self._id)
        print('Hora de llegada: ',self._hora_llegada)
        print('Hora de salida: ',self._hora_salida)
        print('Ciudad de Destino: ', self._ciudad)
    
    def initBoletos(self,id):
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
