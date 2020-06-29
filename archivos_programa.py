
def recorrer_archivo(archivo_entrada, nombre_maximo, nombre_minimo):
    """
    Autor: Francisco
    Ayuda: Pre ---> Ingresa el archivo de entrada
           Post ---> Devuelve True o False si hay cambios en el nombre maximo
                     El nombre maximo y el texto de esa funcion
    """
    linea = archivo_entrada.readline()
    
    while linea:

        if identificar_funciones(linea):
            nombre = nombre_funcion(linea)
            cambio = identificar_alfabeticamente(nombre, nombre_maximo, nombre_minimo)

            if cambio:
                #Guardo la funcion como codigo en el formato pedido
                nombre_maximo = nombre
                

        linea = archivo_entrada.readline()

    return nombre_maximo #Y la funcion que tengo que escribir

def ordenar_funciones(archivo_entrada, archivo_salida_codigo, archivo_salida_com):
    """
    Autor: Francisco
    Ayuda: Pre --> Ingresa el archivo a ordenar y los archivos en los que se van a ordenar
           Post --> Salen ordenadas las funciones por orden alfabetico en el archivo de salida
    """
    nombre_max = 'zzzzzzzz'
    nombre_min = 'aaaaaaaa'
    
    
    while nombre_min != nombre_max:
        nombre_min = recorrer_archivo(archivo_entrada, nombre_max, nombre_min) #Falta la funcion
        archivo_entrada.seek(0) #Vuelvo a empezar con el archivo de entrada
        #Escribo la funcion minima en los dos archivos
        if nombre_min != nombre_max:
            archivo_salida_com.write(nombre_min + "\n")

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
        nombre_maximo = nombre_actual
        cambio = True
    
    return cambio

def main_prueba():
    
    archivo_prueba = open("prueba.txt", 'r')
    archivo_salida = open("salidaPrueba1.txt", 'w')
    ordenar_funciones(archivo_prueba, 0, archivo_salida)
    archivo_prueba.close();archivo_salida.close()

if __name__ == "__main__":
    main_prueba() 