from Avion import Avion

class AvionCarga(Avion):

    def __init__(self,capacidad,volumen,id,modelo,estado):
        super.__init__(self,id,modelo,estado)
        self.capacidad = capacidad
        self.volumen = volumen
    
    def imprimir(self):
        print('--------------------------')
        print('ID Avion:', self._id)
        print('Modelo: ',self._modelo)
        print('Estado: ',self._estado)
        print('Volumen',self.volumen)
        print('Capacidad de carga: ',self.capacidad)
