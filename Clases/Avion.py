from Vuelo import Vuelo

class Avion:
    
    def __init__(self,id,modelo,estado):
        self._id = id;
        self._modelo = modelo
        self._estado = estado
        self._vuelos = []

  
        