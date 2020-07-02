def abrir_archivos(l_ar_entrada):
    """
        PRE: Recibe una lista con nombres de archivos csv 
        POST: Los abre y devuelve una lista con sus manejadores de archivo

    """
    l_manejadores = []
    for ruta in l_ar_entrada:
        l_manejadores.append(open(ruta, "r"))
    return l_manejadores

def leer_archivos(l_manejadores):
    """
        PRE: Recibe una lista con manejadores de archivo csv.
        POST: Devuelve una lista con la linea siguiente de cada archivo.
    """
    l_lineas = []
    for manejador in l_manejadores:
        l_lineas.append(manejador.readline().rstrip('\n').split(','))
    return l_lineas

def cerrar_archivos(archivos):
    """ PRE: Recibe una lista con manejadores de archivos.
        POST: Cierra todos los archivos.
    """
    for archivo in archivos:
        archivo.close()

def devolver_clave_minima(lista, pos_clave):
    """
        PRE:    Recibe una lista de listas y la posicion de la clave
        POST:   Devuelve una tupla con posicion en lista y menor clave
                Si no hay minimo devuelve -1
    """

    return min([(pos, linea[pos_clave]) for pos, linea in enumerate(lista) \
            if  linea[pos_clave] != ''], default = [-1, ''], key = lambda x:x[1])
           
        
def mezclar_archivos(l_ar_entrada, t_ar_salida, clave_pos):
    """ 
        PRE:  Recibe una lista con la ruta de archivos csv (ordenados por clave), 
    el nombre del archivo de salida y la posicion de la clave que los relaciona (debe ser la misma para todos)
        POST: Escribe un archivo de salida unificando todas las lineas manteniendo el orden.

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


