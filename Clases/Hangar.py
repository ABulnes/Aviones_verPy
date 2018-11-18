from AvionCarga import AvionCarga
from AvionComercial import AvionComercial

class Hangar:
    #Constructor que inicializa el hangar
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
        archivo = open('Aviones.csv','a')
        if tipo == 1:
            linea = ','.join([str(avion._id),avion._modelo,avion._estado,'Comercial',str(avion.capacidad),avion.clase])
        else:
            linea = ','.join([str(avion._id),avion._modelo,avion._estado,'Carga',str(avion.capacidad),str(avion.volumen)])
        archivo.write(linea)
        archivo.close()
        return True
    
    #Funcion que obtiene el ultimo id
    def lastID(self):
         return (self.cont_avionesCar+ self.cont_avionesCom)   

    #Funcion que agrega los aviones comerciales a la lista de aviones comerciales
    def agregarAvionComercial(self,modelo,estado,capacidad,clase):
        
        if(self.cont_avionesCom < 10):
            nuevoAvion = AvionComercial(capacidad,clase,self.lastID(),modelo,estado)
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
            nuevoAvion = AvionCarga(capacidad,volumen,self.lastID(),modelo,estado)
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
        print('Deberia eliminar')

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




