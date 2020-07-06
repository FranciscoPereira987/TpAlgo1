MAX_NOMBRE = 'zzzzzzzz'
import mezcla
#-------------------------------Funciones de ordenamiento de archivo---------------------------#
def recorrer_archivo(archivo_entrada, nombre_anterior):
    """
    Autor: Francisco Pereira 
    Ayuda: Pre ---> Ingresa el archivo de entrada
           Post ---> Devuelve el nombre maximo y el texto de esa funcion       
    """
    linea = archivo_entrada.readline()
    nombre_maximo = MAX_NOMBRE
    parametros = ''
    while linea:

        if identificar_funciones(linea):
            nombre = nombre_funcion(linea)
         
            if identificar_alfabeticamente(nombre, nombre_maximo, nombre_anterior):
                #Guardo la funcion como codigo en el formato pedido
                parametros = devolver_parametros(linea)
                nombre_maximo = nombre
                
        linea = archivo_entrada.readline()

    archivo_entrada.seek(0)

    return nombre_maximo, parametros #Y la funcion que tengo que escribir

def ordenar_funciones(archivo_entrada, archivo_salida_codigo, archivo_salida_com):
    """
    Autor: Francisco Pereira
    Ayuda: Pre --> Ingresa el archivo a ordenar y los archivos en los que se van a ordenar
           Post --> Salen ordenadas las funciones por orden alfabetico en el archivo de salida
    """
    nombre_anterior = 'aaaaaaaa'
    nombre_anterior, parametros = recorrer_archivo(archivo_entrada, nombre_anterior)
    
    while nombre_anterior != MAX_NOMBRE:
        linea_a_escribir = f"{nombre_anterior},{parametros},\n"
        archivo_salida_com.write(linea_a_escribir)
        nombre_anterior, parametros = recorrer_archivo(archivo_entrada, nombre_anterior) #Falta la funcion
        #Escribo la funcion minima en los dos archivos

def procesar_entrada(archivo_entrada, rutas_codigo, rutas_com):
    """
    Autor: Francisco
    Ayuda: Pre --> Ingresan los archivos de python, donde va el codigo y donde van los comentarios
           Durante --> Ordena el archivo de codigo y lo reparte en los otros dos
           Post --> Devuelve el proximo archivo de python, cierra los otros dos
    """
    archivo_comentarios = lector_rutas(rutas_com)
    archivo_codigo = lector_rutas(rutas_codigo)
    
    ordenar_funciones(archivo_entrada, archivo_codigo, archivo_comentarios)
    
    mezcla.cerrar_archivos([archivo_codigo, archivo_comentarios])
#-------------------------Funciones de linea----------------------------#    
def identificar_funciones(linea):
    """
    Autor: Francisco Pereira
    Ayuda: Pre --> Ingresa una linea de texto
           Post --> Devuelve True si en esa linea se define una funcion
           False en caso contrario
    """
    if "def " in linea:
        respuesta = True

    else:
        respuesta = False

    return respuesta

def nombre_funcion(linea):
    """
    Autor: Francisco Pereira
    Ayuda: Pre --> Ingresa una linea donde se declara una funcion
           Post --> Devuelve el nombre de la funcion
    """
    indice_max = linea.find("(")
    indice_min = linea.find(" ") + 1
    nombre = linea[indice_min:indice_max]

    return nombre

def identificar_alfabeticamente(nombre_actual, nombre_maximo, nombre_minimo):
    """
    Autor: Francisco Pereira
    Ayudo: Pre --> Ingresan los nombres de funciones (el actual, el maximo y el minimo)
           Post --> Devuelve True si hay cambios False en caso contrario
    """
    cambio = False

    if nombre_actual < nombre_maximo and nombre_actual > nombre_minimo:
        cambio = True
    
    return cambio

def devolver_parametros(linea):
    """
    Autor: Francisco Pereira
    Ayuda:
    Pre --> Ingresa una linea de codigo donde se define una funcion
    Post --> Devuelve los parametros formales separados por /
    """
    indice_inicio = linea.find('(')
    ultimo_indice = linea.find(')') + 1
    parametros = ''
    for caracter in linea[indice_inicio:ultimo_indice]:
        if caracter == ',':
            parametros += '/'
        else:
            parametros += caracter
    
    return parametros
#---------------------Funciones de ruta de archivo----------------------#
def lector_rutas(archivo_rutas):
    """
    Autor: Francisco Pereira
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

def manejar_archivos(archivo_rutas):
    """
    AUTOR: Francisco
    AYUDA:
    Pre --> Ingresa el archivo con las rutas
    durante --> lee la cantidad de lineas en las rutas
    Post --> Devuelve dos archivos txt con las rutas de los archivos a ordenar
    """
    numero = 0
    ruta = archivo_rutas.readline()
    rutas_comentarios = open("rutas_comentarios.txt", 'w')
    rutas_codigo = open("rutas_codigo.txt", 'w')

    while ruta:
        rutas_comentarios.write(f"comentarios_{numero}.csv\n")
        rutas_codigo.write(f"codigo_{numero}.csv\n")
        numero += 1
        ruta = archivo_rutas.readline()
    
    mezcla.cerrar_archivos([rutas_comentarios, rutas_codigo])

    return open("rutas_comentarios.txt", 'r'), open("rutas_codigo.txt", 'r')

#----------------------------Funciones principales (Prueba/ ordenamiento)----------------#
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

def main_ordenamiento():
    """
    Autor: Francisco
    Ayuda: Ordena los archivos de python en archivos csv, uno para codigo, otro para comentarios
    devuelve las rutas a los archivos que tienen las rutas a todos los archivos ordenados 
    """
    rutas  = open("programas.txt", 'r')
    rutas_comentarios, rutas_codigo = manejar_archivos(rutas)
    rutas.seek(0)
    archivo_rutas = lector_rutas(rutas)
    while archivo_rutas:
        procesar_entrada(archivo_rutas, rutas_codigo, rutas_comentarios)
        archivo_rutas = lector_rutas(rutas)

    mezcla.cerrar_archivos([rutas, rutas_codigo, rutas_comentarios])

    return ["rutas_comentarios.csv", "rutas_codigo.csv"]
        
        
if __name__ == "__main__":
    main_prueba() 