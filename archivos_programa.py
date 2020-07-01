MAX_NOMBRE = 'zzzzzzzz'

def recorrer_archivo(archivo_entrada, nombre_anterior):
    """
    Autor: Francisco
    Ayuda: Pre ---> Ingresa el archivo de entrada
           Post ---> Devuelve el nombre maximo y el texto de esa funcion       
    """
    linea = archivo_entrada.readline()
    nombre_maximo = MAX_NOMBRE
    
    while linea:

        if identificar_funciones(linea):
            nombre = nombre_funcion(linea)
         
            if identificar_alfabeticamente(nombre, nombre_maximo, nombre_anterior):
                #Guardo la funcion como codigo en el formato pedido
                nombre_maximo = nombre
                
        linea = archivo_entrada.readline()

    archivo_entrada.seek(0)

    return nombre_maximo #Y la funcion que tengo que escribir

def ordenar_funciones(archivo_entrada, archivo_salida_codigo, archivo_salida_com):
    """
    Autor: Francisco
    Ayuda: Pre --> Ingresa el archivo a ordenar y los archivos en los que se van a ordenar
           Post --> Salen ordenadas las funciones por orden alfabetico en el archivo de salida
    """
    
    nombre_anterior = 'aaaaaaaa'
    nombre_anterior = recorrer_archivo(archivo_entrada, nombre_anterior)
    
    while nombre_anterior != MAX_NOMBRE:
        archivo_salida_com.write(nombre_anterior + ",,\n")
        nombre_anterior = recorrer_archivo(archivo_entrada, nombre_anterior) #Falta la funcion
        #Escribo la funcion minima en los dos archivos
        
            

def identificar_funciones(linea):
    """
    Autor: Francisco
    Ayuda: Pre --> Ingresa una linea de texto
           Post --> Devuelve True si en esa linea se define una funcion
           False en caso contrario
    """
    if "def" in linea:
        respuesta = True

    else:
        respuesta = False

    return respuesta

def nombre_funcion(linea):
    """
    Autor: Francisco
    Ayuda: Pre --> Ingresa una linea donde se declara una funcion
           Post --> Devuelve el nombre de la funcion
    """
    indice_max = linea.find("(")
    indice_min = linea.find(" ") + 1
    nombre = linea[indice_min:indice_max]

    return nombre

def identificar_alfabeticamente(nombre_actual, nombre_maximo, nombre_minimo):
    """
    Autor: Francisco
    Ayudo: Pre --> Ingresan los nombres de funciones (el actual, el maximo y el minimo)
           Post --> Devuelve True si hay cambios False en caso contrario
    """
    cambio = False

    if nombre_actual < nombre_maximo and nombre_actual > nombre_minimo:
        cambio = True
    
    return cambio
def lector_rutas(archivo_rutas):
    """
    Autor: Francisco
    Ayuda: Pre --> Ingresa el archivo que contiene las rutas
            Post --> Devuelve un archivo abierto
    """
    ruta = archivo_rutas.readline()
    if ruta:
    
        ruta = ruta.rstrip('\n')
        archivo = open(ruta, 'r')
    else:
        archivo = ""

    return archivo

def main_prueba():
    
    archivo_rutas = open("programas.txt", 'r')
    archivo_prueba = lector_rutas(archivo_rutas)
    numero = 0
    while archivo_prueba:
        archivo_salida = open(f"salidaPrueba{numero}.csv", 'w')
        ordenar_funciones(archivo_prueba, 0, archivo_salida)
        archivo_prueba.close();archivo_salida.close()
        archivo_prueba = lector_rutas(archivo_rutas)
        numero += 1
        

if __name__ == "__main__":
    main_prueba() 