from Boleto import Boleto

class Vuelo:

    def __init__(self,id,hora_llegada,hora_salida,ciudad):
        self._id = id
        self._hora_llegada = hora_llegada
        self._hora_salida = hora_salida
        self._ciudad = ciudad
        self._pasajeros = []

    def imprimir(self):
        print('--------------------')
        print('ID Vuelo: ',self._id)
        print('Hora de llegada: ',self._hora_llegada)
        print('Hora de salida: ',self._hora_salida)
        print('Ciudad de Destino: ', self._ciudad)
    