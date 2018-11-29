from AvionCarga import AvionCarga
from AvionComercial import AvionComercial
from Archivo import Archivo

class Hangar:
    #Constructor que inicializa el hangar
    def __init__(self):
        self.lista_avionesComerciales = []
        self.lista_avionesCarga = []
        self.cont_avionesCar = 0
        self.cont_avionesCom = 0
        self.listaPrecios = []
        try:
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
                    avionComercial = AvionComercial(capacidad,atributo,id,modelo,estado,precio_eco,precio_ejec)
                    self.lista_avionesComerciales.append(avionComercial)
                    self.cont_avionesCom += 1
                elif tipo == 'Carga':
                    avionCarga = AvionCarga(capacidad,atributo,id,modelo,estado,0,precio_carga)
                    self.lista_avionesCarga.append(avionCarga)
                    self.cont_avionesCar += 1
            archivo.close()
            archivo2 = open('Precios.csv' , 'r')
            for linea2 in archivo2:
                partes = linea2.split(',')
                self.listaPrecios.append(float(partes[2]))
            archivo2.close()

        except:
             print('Ocurrio un error al abrir el archivo')

    #Imprime los aviones comerciales 
    def imprimirComerciales(self):
        print('--------------------------------')
        print('Aviones Comerciales')
        print('--------------------------------')
        for i in self.lista_avionesComerciales:
            i.imprimir()
    #Imprime los avones de carga
    def imprimirCarga(self):
        print('--------------------------------')
        print('Aviones de Carga')
        print('--------------------------------')
        for i in self.lista_avionesCarga:
            i.imprimir()

    #Imprime todos los aviones
    def imprimirAviones(self):
        self.imprimirComerciales()
        self.imprimirCarga()      
        
    #Funcion que obtiene los aviones restantes del hangar
    def avionesRestantes(self):
        return 20 - (self.cont_avionesCar + self.cont_avionesCom)
    
    #Funcion que agrega el avion al archivo
    def inAvion(self,avion,tipo):
        try:
            archivo = open('Aviones.csv','a')
            if tipo == 1:
                linea = ','.join([str(avion._id),avion._modelo,avion._estado,'Comercial',str(avion.capacidad),avion.clase])
            else:
                linea = ','.join([str(avion._id),avion._modelo,avion._estado,'Carga',str(avion.capacidad),str(avion.volumen)])
            archivo.write(linea)
            archivo.close()
            return True
        except:
             print('Ocurrio un error al abrir el archivo')
    
    #Funcion que obtiene el ultimo id
    def lastID(self):
         return (self.cont_avionesCar+ self.cont_avionesCom)   

    #Funcion que agrega los aviones comerciales a la lista de aviones comerciales
    def agregarAvionComercial(self,modelo,estado,capacidad,clase):
        
        if(self.cont_avionesCom < 10):
            nuevoAvion = AvionComercial(capacidad,clase,self.lastID(),modelo,estado, precio_eco, precio_ejec)
            if(self.inAvion(nuevoAvion,1)):
                self.lista_avionesComerciales.append(nuevoAvion)
                self.cont_avionesCom +=1
                print('Se ha agregado el avion correctamente')
            else:
                print('Ocurrio un error al intentar agregar el avion')
        else:
            print('No se pueden agregar mas aviones comerciales')
            print('Limite alcanzado: 10 Aviones')

    #Funcion que agrega los aviones comerciales a la lista de aviones comerciales
    def agregarAvionCarga(self,modelo,estado,capacidad,volumen):
        
        if(self.cont_avionesCar < 10):
            nuevoAvion = AvionCarga(capacidad,volumen,self.lastID(),modelo,estado,0,precio_carga)
            if(self.inAvion(nuevoAvion,1)):
                self.lista_avionesCarga.append(nuevoAvion)
                self.cont_avionesCar +=1
                print('Se ha agregado el avion correctamente')
            else:
                print('Ocurrio un error al intentar agregar el avion')
        else:
            print('No se pueden agregar mas aviones de carga')
            print('Limite alcanzado: 10 Aviones')    
   
    #Funcion que elimna el avion del archivo 
    def delAvion(self,id):
        try:
            op_ar = Archivo()
            op_ar.eliminar('Aviones.csv',id)
            return True
        except:
            print('Ocurrio un error al eliminar el avion')
            return False

    #Funcion que permite eliminar los aviones de la lista
    def eliminarAvion(self,id):
        if (self.delAvion(id)):
            for i,j in self.lista_avionesComerciales,self.lista_avionesCarga:
                if(i._id == id):
                    self.lista_avionesComerciales.remove(i)
                    self.cont_avionesCom -= 1
                    print('Se elimino el avion correctamente')
                    return
                elif (j._id == id):
                    self.lista_avionesCarga.remove(j)
                    self.cont_avionesCar -= 1
                    print('Se elimino el avion correctamente')
                    return
           
        else:
            print('El avion especificado no existe')

    def verAvionesDisponibles(self):
        print('--------------------------------')
        print('Aviones Disponibles')
        print('--------------------------------')
        for i in self.lista_avionesComerciales:
            if i._estado == 'B':
                i.imprimir()
        
        for j in self.lista_avionesCarga:
             if j._estado == 'B':
                j.imprimir()

    #Funcion que permite reservar un vuelo 
    def reservarVuelo(self,idAvion,idVuelo,nombre,asiento):
        for i in self.lista_avionesComerciales:
            if(i._id == idAvion):
                for vuelo in i._vuelos:
                    if(vuelo._id == idVuelo and (vuelo.num_pasajeros < i.capacidad)):
                        if(vuelo.reservar(nombre,asiento)):
                            print('Se reservo el vuelo correctamente')
                            return
                        else:
                            print('Ocurrio un error al guardar el vuelo')
                            return

    #Funcion que cancela el vuelo
    def cancelarVuelo(self,nombre):
        for avion in self.lista_avionesComerciales:
            for vuelos in avion._vuelos:
                for pasajero in vuelos._pasajeros:
                    if pasajero._nombre == nombre:
                        if vuelos.eliminarPasajero(nombre):
                            print('Se ha eliminado la reservacion del vuelo correctamente')
                            return
                        else:
                            print('Ocurrio un error al eliminar el pasajero')
                            return 

    #Funcion que permite cambiar el estado del avion
    def cambiarEstado(self, id, estadonuevo):
        for i in self.lista_avionesComerciales:
            if(i._id == id):
                i._estado = estadonuevo
            print('El avion comercial con ID ' + i._id + ' cambio de estado correctamente.\n')
            break

        for j in self.lista_avionesCarga:
            if(j._id == id):
                j._estado = estadonuevo
            print('El avion de carga con ID ' + j._id + ' cambio de estado correctamente.\n')
            break

    #Funcion que permite ver los vuelos
    def verVuelos(self):
        print('-------------------------------------\n')
        print('Historial de Vuelos\n')    
        print('-------------------------------------\n')

        print('Vuelos Comerciales\n')
        for i in self.lista_avionesComerciales:
            print('Modelo: ' + i._modelo + '\n')
            print('Vuelos: ' + i._vuelos + '\n')
        
        print('Vuelos de Carga\n')
        for j in self.lista_avionesCarga:
            print('Modelo: ' + i._modelo + '\n')
            print('Vuelos: ' + i._vuelos + '\n')

    #Funcion que genera las ganancias
    def generarGanancia(self):
        ganancia_total = 0
        x = 0
        y = 0
        for i in self.lista_avionesComerciales:
            for vuelo in i._vuelos:
                if(i.clase == 'Ejecutiva'):
                    x += vuelo.num_pasajeros * self.listaPrecios[0]
                elif(i.clase == 'Economica'):
                    x += vuelo.num_pasajeros * self.listaPrecios[1]

        for j in self.lista_avionesCarga:
            for vuelo in j._vuelos:
                y += vuelo.capacidadactual * self.listaPrecios[2]
        ganancia_total = x + y
        return ganancia_total
    

        
