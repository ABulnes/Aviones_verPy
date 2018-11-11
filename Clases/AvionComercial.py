from Avion import Avion

class AvionComercial(Avion):

    def __init__(self,capacidad,clase,id,modelo,estado):
        super.__init__(self,id,modelo,estado)
        self.capacidad = capacidad
        self.clase = clase
    
    def imprimir(self):
        print('--------------------------')
        print('ID Avion:', self._id)
        print('Modelo: ',self._modelo)
        print('Estado: ',self._estado)
        print('Clase: ',self.clase)
        print('Capacidad de pasajeros: ',self.capacidad)
