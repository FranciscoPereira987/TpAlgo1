import apareo_csv
# ----------------------------- #.

# ---- RUTAS DE ARCHIVOS ------ #.

#AR_FUENTE_UNICO = "fuente_unico.csv"
#AR_COMENTARIOS  = "comentarios.csv"
#SALIDA = "/archivos_prueba/prueba_info/info_salida.txt"
AR_FUENTE_UNICO = "archivos_prueba/prueba_apareo/pruebaE01.csv"
AR_COMENTARIOS = "archivos_prueba/prueba_apareo/pruebaE02.csv"



# -------- MENSAJES ----------- #.

ENCABEZADO_1 = "Informe de desarrollo por autor\n\n" 

# --ESTRUCTURAS DE ARCHIVOS---- #.
AR_SALIDA = "archivos_prueba/prueba_info/participacion.txt"
D_ENTRADA = {
        "funcion_a": 0, 
        "p_formales": 1, 
        "modulo": 2, 
        "instrucciones": 3,
        "funcion_b": 4,
        "autor": 5,
        "ayuda": 6,
        "comentarios": 7
        }
D_FUENTES = {
        "funcion": 0, 
        "p_formales": 1, 
        "modulo": 2, 
        "instrucciones": 3,
        }
D_COMENTARIOS = {
        "funcion": 0,
        "autor": 1,
        "ayuda": 2,
        "comentarios": 3
        }

INDICE_A = ["funcion_a", "instrucciones"]
POS_CLAVE = D_ENTRADA["autor"]
LONG_CAMPOS = 30
T_CLAVE = "autor"
CLAVE_F_UNICO = 0
CLAVE_COMENTARIOS = 0

def listar_campos_csv(n_archivo, posicion):
    """
    [Autor: Ivan Coronel]
    [Ayuda: Recibe el nombre de un archivo csv y una posicion.
            Lo lee completo y devuelve los distintos valores que
            contiene ese campo ordenado.]
    """
    l_valores = []
    with open(n_archivo, "r") as archivo:
        linea = archivo.readline()
        while linea != "":
            l_campos = linea.rstrip('\n').split(',')
            if l_campos[posicion] not in l_valores:
                l_valores.append(l_campos[posicion])
            linea = archivo.readline()
    return sorted(l_valores)


def grabar_participacion_csv(arc_entrada, ar_salida, autor, func_cantidad):
    """
        [Autor: Ivan Coronel]
        [Ayuda: Busca en el archivo de entrada los registros
        que coincidan en la posicion clave con el valor dado y los
        graba en el archivo de salida]
    """
    total_funciones = 0
    total_instrucciones = 0
    with open(arc_entrada, "r") as ar_entrada:
        linea = ar_entrada.readline()
        l_linea = leer_csva(linea, D_FUENTES["instrucciones"], D_COMENTARIOS["comentarios"])
        funcion_ant = ''
        while linea != '':
            l_linea = leer_csva(linea, D_FUENTES["instrucciones"], D_COMENTARIOS["comentarios"])
            if l_linea[D_ENTRADA["autor"]] == autor \
                    and l_linea[D_ENTRADA["funcion_a"]] > funcion_ant:
                funcion, instrucciones = seleccionar_campos_lista(l_linea, D_ENTRADA, INDICE_A)    
                funcion_ant = funcion
                cant_instrucciones = len(instrucciones.split(";"))
                total_instrucciones += cant_instrucciones
                total_funciones += 1
                grabar_tabla(("\t" + funcion, str(cant_instrucciones)), ar_salida)
            linea = ar_entrada.readline()
        porcentaje = (total_funciones * 100) / func_cantidad
        grabar_tabla(("\t" + str(total_funciones) + " Funciones - Lineas"  , str(total_instrucciones) + "\t" + str(round(porcentaje)) + '%'), ar_salida)
        grabar_tabla(("\n"), ar_salida)
    return total_funciones, total_instrucciones
    

def grabar_tabla(l_campos, salida):
    """
        [Autor: Ivan Coronel]
        [Ayuda: Recibe una lista de cadenas y un archivo de salida
                Las formatea con una longitud constante.
                Si la supera no la corta y se desfasa el campo.]
    """
    linea = ""
    for campo in l_campos:
        linea = linea + campo.ljust(LONG_CAMPOS, ' ') 
    linea += "\n"
    salida.write(linea)
    print(linea)

def seleccionar_campos_lista(lista, diccionario, campos):
    """ 
        [Autor: Ivan Coronel]
        [Ayuda: Se recibe una lista con valores, una lista 
                con nombres de los campos a seleccionar y 
                un diccionario con la relacion entre nombre de 
                campo y posicion.
                Devuelve una lista con los campos de la lista
                que se han seleccionado.
    """
    return [lista[diccionario[campo]] for campo in campos]


def combinar_campos_lista(lista, pos_ini, pos_fin, separador):
    """
        [Autor: Ivan Coronel]
        [Ayuda: Recibe una lista, posiciones de inicio, de fin,
                y un separador.
                Las posiciones que van entre pos_ini y pos_fin,
                se combinan en un solo elemento de la lista
                separados por el caracter dado en separador.
                Es conjunto abierto en pos_fin.
    """
    return lista[0:pos_ini] + [separador.join(lista[pos_ini:pos_fin])] + lista[pos_fin:]


def leer_csva(linea_csva, clave_1, clave_2):
    """ 
        [Autor: Ivan Coronel]
        [Ayuda: Separa las lineas en formato csva en csv. ]
    """
    l_1, l_2 = linea_csva.rstrip('\n').split(';')
    l_1_csv = l_1.rstrip('\n').split(',') 
    l_1_csv_combinado = combinar_campos_lista(l_1_csv, clave_1, len(l_1_csv), ';')
    l_2_csv = l_2.split(',') 
    l_2_csv_combinado = combinar_campos_lista(l_2_csv, clave_2, len(l_1_csv), ';')

    return l_1_csv_combinado + l_2_csv_combinado

def informar_participacion():
    """
        [Autor: Ivan Coronel]
        [Ayuda  Lee los archivos de las rutas de las constantes
                AR_FUENTE_UNICO y AR_COMENTARIOS en formato 
                dado por los diccionarios asociados.
                Genera informe sobre la participacion de cada
                desarrollador en un sistema. ]
    """

    totales_lineas = 0
    autores = listar_campos_csv(AR_COMENTARIOS, D_COMENTARIOS["autor"])
    with open(AR_SALIDA, 'w') as ar_salida:
        grabar_tabla([ENCABEZADO_1], ar_salida)
        t_apareo, total_funciones = apareo_csv.aparear_csv(AR_FUENTE_UNICO, AR_COMENTARIOS, CLAVE_F_UNICO, CLAVE_COMENTARIOS)
        while autores:
            autor = autores.pop()
            grabar_tabla(("\tAutor: ".rjust(4, " "), autor, '\n'), ar_salida)
            grabar_tabla(("\tFuncion", "Lineas"), ar_salida)
            grabar_tabla((["\t" + "-".ljust(LONG_CAMPOS * 2, '-')]), ar_salida)
            cant_funciones_autor, cant_instrucciones_autor = grabar_participacion_csv(t_apareo, ar_salida, autor, total_funciones)
            totales_lineas += cant_instrucciones_autor
        grabar_tabla(("Total: " + str(total_funciones) + " Funciones - Lineas"  , str(totales_lineas)), ar_salida)
