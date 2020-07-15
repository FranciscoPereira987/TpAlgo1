import os
import mezcla
import sep_cod_com

MAX_NOMBRE = 'zzzzzzzz'


def recorrer_archivo(archivo_entrada, nombre_anterior):
    """
    [Autor: Francisco Pereira] 
    [Ayuda: Pre ---> Ingresa el archivo de entrada
           Post ---> Devuelve el nombre maximo y el texto de esa funcion]       
    """
    linea = archivo_entrada.readline()
    nombre_maximo = MAX_NOMBRE
    parametros = l_cod = l_com = ''
    
    while linea:

        if identificar_funciones(linea):
            nombre = nombre_funcion(linea)
         
            if identificar_alfabeticamente(nombre, nombre_maximo, nombre_anterior):
                parametros = devolver_parametros(linea)
                linea, l_cod, l_com = sep_cod_com.leer_funcion(archivo_entrada) 
                nombre_maximo = nombre
            
            else:
                linea = archivo_entrada.readline()
        else:
            linea = archivo_entrada.readline()

    archivo_entrada.seek(0)

    return nombre_maximo, parametros, l_cod, l_com 

def ordenar_funciones(archivo_entrada, archivo_salida_cod, archivo_salida_com, nombre_modulo):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Pre --> Ingresa el archivo a ordenar y los archivos en los que se van a ordenar
           Post --> Salen ordenadas las funciones por orden alfabetico en el archivo de salida]
    """
    nombre_anterior = 'aaaaaaaa'
    nombre_anterior, parametros, l_cod, l_com =\
    recorrer_archivo(archivo_entrada, nombre_anterior)

    

    while nombre_anterior != MAX_NOMBRE:
        l_cod, l_com = lista_a_string(l_cod, l_com)
        linea_cod = f"{nombre_anterior},{parametros},{nombre_modulo}," + l_cod + '\n'
        linea_com = f"{nombre_anterior}," + l_com + '\n'
        archivo_salida_cod.write(linea_cod)
        archivo_salida_com.write(linea_com)
        nombre_anterior, parametros, l_cod, l_com = \
        recorrer_archivo(archivo_entrada, nombre_anterior)
        
        #Escribo la funcion minima en los dos archivos

def procesar_entrada(archivo_entrada, rutas_codigo, rutas_com, nombre_modulo):
    """
    [Autor: Francisco]
    [Ayuda: Pre --> Ingresan los archivos de python, donde va el codigo y donde van los comentarios
           Durante --> Ordena el archivo de codigo y lo reparte en los otros dos
           Post --> Cierra los archivos de codigo y comentarios]
    """
    archivo_comentarios, mod_false = lector_rutas(rutas_com)
    archivo_codigo, mod_false = lector_rutas(rutas_codigo) #Mod_false esta para guardar un string vacio que no sirve
    
    ordenar_funciones(archivo_entrada, archivo_codigo, archivo_comentarios, nombre_modulo)
    
    mezcla.cerrar_archivos([archivo_codigo, archivo_comentarios])


def identificar_funciones(linea):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Pre --> Ingresa una linea de texto
           Post --> Devuelve True si en esa linea se define una funcion
           False en caso contrario]
    """

    return "def " in linea

def nombre_funcion(linea):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Pre --> Ingresa una linea donde se declara una funcion
           Post --> Devuelve el nombre de la funcion]
    """
    indice_max = linea.find("(")
    indice_min = linea.find(" ") + 1
    nombre = linea[indice_min:indice_max]

    return nombre

def identificar_alfabeticamente(nombre_actual, nombre_maximo, nombre_minimo):
    """
    [Autor: Francisco Pereira]
    [Ayudo: Pre --> Ingresan los nombres de funciones (el actual, el maximo y el minimo)
           Post --> Devuelve True si hay cambios False en caso contrario]
    """
    
    return nombre_actual < nombre_maximo and nombre_actual > nombre_minimo

def devolver_parametros(linea):
    """
    [Autor: Francisco Pereira]
   [Ayuda:
    Pre --> Ingresa una linea de codigo donde se define una funcion
    Post --> Devuelve los parametros formales separados por /]
    """
    indice_inicio = linea.find('(')
    ultimo_indice = linea.find(')') + 1

    parametros = linea[indice_inicio:ultimo_indice].replace(',', '/')
    
    
    return parametros

def nombre_modulo(linea):
    """
    [Autor: Francisco]
    [Ayuda:
    Pre --> Ingresa una linea donde se encuentra la ruta a un archivo de python
    Post --> Devuelve el nombre del archivo de python]
    """
    ultimo_indice = linea.find(".py")
    if os.name == "nt":
        primer_indice = len(linea) - linea[::-1].find("\\")
    else:
        primer_indice = len(linea) - linea[::-1].find("/")
        
    return linea[primer_indice:ultimo_indice]

def lista_a_string(l_codigo, l_comentarios):

    str_codigo = ','.join(l_codigo)
    str_comentarios = ','.join(l_comentarios)

    return str_codigo, str_comentarios


def lector_rutas(archivo_rutas, ruta_py = False):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Pre --> Ingresa el archivo que contiene las rutas y una opcional
                    ruta_py que si es True genera tambien el nombre del modulo
            Post --> Devuelve un archivo abierto y un nombre de modulo 
            el nombre de modulo esta vacio si ruta_py se pasa como False]
    """
    ruta = archivo_rutas.readline()
    if ruta:
        if ruta_py:
            modulo = nombre_modulo(ruta)
        else:
            modulo = ""
        ruta = ruta.rstrip('\n')
        archivo = open(ruta, 'r')

    else:
        archivo = modulo = ""
        
    return archivo, modulo

def manejar_archivos(archivo_rutas):
    """
    [AUTOR: Francisco Pereira]
    [AYUDA:
    Pre --> Ingresa el archivo con las rutas
    durante --> lee la cantidad de lineas en las rutas
    Post --> Devuelve dos archivos txt con las rutas de los archivos a ordenar]
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


def main_prueba():
    
    archivo_rutas = open("programas.txt", 'r')
    archivo_prueba, modulo = lector_rutas(archivo_rutas, True)
    numero = 0
    while archivo_prueba:
        archivo_salida_com = open(f"comentarios{numero}.csv", 'w')
        archivo_salida_cod = open(f"codigo{numero}.csv", 'w')
        ordenar_funciones(archivo_prueba, archivo_salida_cod, archivo_salida_com, modulo)
        mezcla.cerrar_archivos([archivo_prueba,archivo_salida_cod, archivo_salida_com])
        archivo_prueba, modulo = lector_rutas(archivo_rutas, True)
        numero += 1

    

def main_ordenamiento():
    """
    [Autor: Francisco Pereira]
    [Ayuda: Ordena los archivos de python en archivos csv, uno para codigo, otro para comentarios
    devuelve las rutas a los archivos que tienen las rutas a todos los archivos ordenados] 
    """
    rutas  = open("programas.txt", 'r')
    rutas_comentarios, rutas_codigo = manejar_archivos(rutas)
    rutas.seek(0)
    archivo_rutas, nombre_modulo = lector_rutas(rutas, True)
    while archivo_rutas:
        procesar_entrada(archivo_rutas, rutas_codigo, rutas_comentarios, nombre_modulo)
        archivo_rutas, nombre_modulo = lector_rutas(rutas, True)

    mezcla.cerrar_archivos([rutas, rutas_codigo, rutas_comentarios])

    return ["rutas_comentarios.csv", "rutas_codigo.csv"]
        
        
if __name__ == "__main__":
    main_prueba() 