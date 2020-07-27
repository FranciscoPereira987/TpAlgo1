import str_hnd
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

        if str_hnd.identificar_funciones(linea):
            nombre = str_hnd.nombre_funcion(linea)
         
            if str_hnd.identificar_alfabeticamente(nombre, nombre_maximo, nombre_anterior):
                parametros = str_hnd.devolver_parametros(linea)
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
        l_cod, l_com = str_hnd.procesar_funcion(l_cod, l_com)
        linea_cod = f"{nombre_anterior},{parametros},{nombre_modulo},{l_cod}\n"
        linea_com = f"{nombre_anterior},{l_com}\n"
        archivo_salida_cod.write(linea_cod)
        archivo_salida_com.write(linea_com)
        nombre_anterior, parametros, l_cod, l_com = \
        recorrer_archivo(archivo_entrada, nombre_anterior)
        
        #Escribo la funcion minima en los dos archivos

def procesar_entrada(archivo_entrada, rutas_codigo, rutas_com, nombre_modulo):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Pre --> Ingresan los archivos de python, donde va el codigo y donde van los comentarios
           Durante --> Ordena el archivo de codigo y lo reparte en los otros dos
           Post --> Cierra los archivos de codigo y comentarios]
    """
    archivo_comentarios, archivo_codigo  = generar_archivos(rutas_codigo, rutas_com)
    
    
    ordenar_funciones(archivo_entrada, archivo_codigo, archivo_comentarios, nombre_modulo)
    
    mezcla.cerrar_archivos([archivo_codigo, archivo_comentarios])




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
            modulo = str_hnd.nombre_modulo(ruta)
        else:
            modulo = ""
        ruta = ruta.rstrip('\n')
        archivo = open(ruta, 'r')

    else:
        archivo = modulo = ""
        
    return archivo, modulo

def manejar_archivos(archivo_rutas):
    """
    [Autor: Francisco Pereira]
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

def generar_archivos(rutas_cod, rutas_com):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Genera los archivos de codigo y comentario
    en las rutas pasadas como paramentro]
    """
    ruta_cod, ruta_com = rutas_cod.readline(), rutas_com.readline()
    ruta_cod = ruta_cod.rstrip('\n')
    ruta_com = ruta_com.rstrip('\n')
    archivo_1 = open(ruta_cod, 'w')
    archivo_2 = open(ruta_com, 'w')
    
    return archivo_2, archivo_1


def main_ordenamiento():
    """
    [Autor: Francisco Pereira]
    [Ayuda: Ordena los archivos de python en archivos csv, uno para codigo, otro para comentarios
    devuelve las rutas a los archivos que tienen las rutas a todos los archivos ordenados] 
    """
    rutas  = open("programas.txt", 'r')
    rutas_comentarios, rutas_codigo = manejar_archivos(rutas)
    rutas.seek(0)
    archivo_entrada, nombre_modulo = lector_rutas(rutas, True)
    while archivo_entrada:
        
        procesar_entrada(archivo_entrada, rutas_codigo, rutas_comentarios, nombre_modulo)
        archivo_entrada, nombre_modulo = lector_rutas(rutas, True)

    mezcla.cerrar_archivos([rutas, rutas_codigo, rutas_comentarios])

    return ["rutas_comentarios.txt", "rutas_codigo.txt"]
        
        
if __name__ == "__main__":
    main_ordenamiento() 