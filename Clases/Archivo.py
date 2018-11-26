class Archivo:

    def eliminar(self,nombre_archivo,identificador):
        archivo = open(nombre_archivo,'r')
        file = archivo.read()
        posicion_init = file.find(str(identificador))
        temp_init = file[:posicion_init]
        posicion_end = file.find(str(identificador+1))
        temp_end = file[posicion_end:len(file)-1]
        file = temp_init + temp_end
        archivo.close()
        archivo = open(nombre_archivo,'w+')
        archivo.write(file)
        archivo.close()