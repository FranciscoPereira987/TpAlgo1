def abrir_archivos(l_ar_entrada):
    """
        [AUTOR: Ivan Coronel]
        [AYUDA: Recibe una lista con nombres de archivos csv. 
                Los abre y devuelve una lista con sus manejadores de archivo.]
    """
    l_manejadores = []
    for ruta in l_ar_entrada:
        l_manejadores.append(open(ruta, "r"))
    return l_manejadores

def leer_archivos(l_manejadores):
    """
        [AUTOR: Ivan Coronel]
        [AYUDA: Recibe una lista con manejadores de archivo csv.
                Devuelve una lista con la linea siguiente de cada archivo.]
    """
    l_lineas = []
    for manejador in l_manejadores:
        l_lineas.append(manejador.readline().rstrip('\n').split(','))
    return l_lineas

def cerrar_archivos(archivos):
    """ 
        [AUTOR: Ivan Coronel]
        [AYUDA: Recibe una lista con manejadores de archivos. 
                Cierra todos los archivos.]
    """
    for archivo in archivos:
        archivo.close()

def devolver_clave_minima(lista, pos_clave):
    """
        [AUTOR: Ivan Coronel]
        [AYUDA: Recibe una lista de listas y la posicion de la clave.
                Devuelve una tupla con posicion en lista y menor clave
                Si no hay minimo devuelve -1.]
    """

    return min([(pos, linea[pos_clave]) for pos, linea in enumerate(lista) \
            if  linea[pos_clave] != ''], default = [-1, ''], key = lambda x:x[1])
           
        
def mezclar_archivos(l_ar_entrada, t_ar_salida, clave_pos):
    """ 
        [AUTOR: Ivan Coronel]
        [AYUDA: Recibe una lista con la ruta de archivos csv ordenados por
                clave, el nombre de archivo de salida, y la posicion de la 
                clave que los relaciona.
                Todos los archivos deben tener la clave en la misma posicion. 
                Escribe un archivo de salida unificando todas las lineas 
                manteniendo el orden.]

    """

    l_manejadores = abrir_archivos(l_ar_entrada)
    l_lineas = leer_archivos(l_manejadores)
    pos_min, l_min = devolver_clave_minima(l_lineas, 0)
    ar_salida = open(t_ar_salida, "w")
        
    while pos_min != -1:
        ar_salida.write(",".join(l_lineas[pos_min]) + "\n")
        l_lineas[pos_min] = l_manejadores[pos_min].readline().rstrip('\n').split(",")
        pos_min, l_min = devolver_clave_minima(l_lineas, 0)

    cerrar_archivos(l_manejadores + [ar_salida])


