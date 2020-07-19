import apareo_csv

#AR_FUENTE_UNICO = "fuente_unico.csv"
#AR_COMENTARIOS  = "comentarios.csv"
AR_FUENTE_UNICO = "archivos_prueba/prueba_apareo/pruebaE01.csv"
AR_COMENTARIOS = "archivos_prueba/prueba_apareo/pruebaE02.csv"
AR_SALIDA = "archivos_prueba/prueba_info/participacion.txt"
#SALIDA = "/archivos_prueba/prueba_info/info_salida.txt"
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


def devolver_maximo_siguiente(archivo, posicion_clave, max_anterior):
    """ 
        [AUTOR: Ivan Coronel]
        [AYUDA: Recibe nombre de archivo, posicion de la clave y clave maxima
        anterior, si no hay anterior se debe recibir ''. 
        Devuelve el valor maximo siguiente.
    """
    maximo = "" 
    linea_max = ""
    linea = archivo.readline()
    clave = leer_csva(linea, D_FUENTES["instrucciones"], D_COMENTARIOS["comentarios"])[posicion_clave]
    while linea != "":
        clave = leer_csva(linea, D_FUENTES["instrucciones"], D_COMENTARIOS["comentarios"])[posicion_clave]
        if (clave < max_anterior and clave > maximo) or (max_anterior == '' and  clave > maximo):
            maximo = clave
            linea_max = linea
        linea = archivo.readline()
    return maximo, linea_max 
    

def grabar_participacion_csv(ar_entrada, ar_salida, clave, linea):
    """
        [AUTOR: Ivan Coronel]
        [AYUDA: Busca en el archivo de entrada los registros
        que coincidan en la posicion clave con el valor dado y los
        graba en el archivo de salida]
    """
    grabar_tabla(("\tFuncion", "Lineas"), AR_SALIDA)
    grabar_tabla((["\t" + "-".ljust(LONG_CAMPOS * 2, '-')]), AR_SALIDA)
    l_linea = leer_csva(linea, D_FUENTES["instrucciones"], D_COMENTARIOS["comentarios"])
    clave_valor = l_linea[D_ENTRADA[clave]]
    funcion_ant = ''
    while linea != '':
        l_linea = leer_csva(linea, D_FUENTES["instrucciones"], D_COMENTARIOS["comentarios"])
        if l_linea[D_ENTRADA[clave]] == clave_valor \
                and l_linea[D_ENTRADA["funcion_a"]] > funcion_ant:
            funcion, comentarios = seleccionar_campos_lista(l_linea, D_ENTRADA, INDICE_A)    
            funcion_ant = funcion
            cant_comentarios = len(comentarios.split(";"))
            grabar_tabla(("\t" + funcion, str(cant_comentarios)), AR_SALIDA)
        linea = ar_entrada.readline()
    grabar_tabla(("\n"), AR_SALIDA)

def grabar_tabla(l_campos, t_archivo):
    """
        [Autor: Ivan Coronel]
        [Ayuda:]
    """

    with open(t_archivo, 'a') as salida:
        for campo in l_campos:
            salida.write(campo.ljust(LONG_CAMPOS, ' '))
        salida.write('\n')

def seleccionar_campos_lista(lista, diccionario, campos):
    """ 
        [Autor: Ivan Coronel]
        [Ayuda: Recibe dos listas, lista contiene la informacion
        y campos contiene las posiciones a seleccionar.
        Se devuelve una lista que solo contendra los campos seleccionados.
    """
    return [lista[diccionario[campo]] for campo in campos]


def combinar_campos_lista(lista, pos_ini, pos_fin, separador):
    return lista[0:pos_ini] + [separador.join(lista[pos_ini:pos_fin])] + lista[pos_fin:]


def leer_csva(linea_csva, clave_1, clave_2):
    """ 
        [Ayuda: Separa las lineas en formato csva en csv ]
        [Autor: Ivan Coronel]
    """
    l_1, l_2 = linea_csva.rstrip('\n').split(';')
    l_1_csv = l_1.rstrip('\n').split(',') 
    l_1_csv_combinado = combinar_campos_lista(l_1_csv, clave_1, len(l_1_csv), ';')
    l_2_csv = l_2.split(',') 
    l_2_csv_combinado = combinar_campos_lista(l_2_csv, clave_2, len(l_1_csv), ';')

    return l_1_csv_combinado + l_2_csv_combinado

def informar_participacion():
    """
        [Ayuda:]
        [Autor: Ivan Coronel]
    """
    grabar_tabla(["Informe de desarrollo por autor\n\n"], AR_SALIDA)
    t_apareo = apareo_csv.aparear_csv(AR_FUENTE_UNICO, AR_COMENTARIOS, CLAVE_F_UNICO, CLAVE_COMENTARIOS)
    apareo = open(t_apareo, 'r')
    max_ant = ''
    maximo, linea_max = devolver_maximo_siguiente(apareo, POS_CLAVE, '') 
    apareo.close()
    apareo = open(t_apareo, 'r')
    while max_ant != maximo and maximo != '':
        grabar_tabla(("\tAutor: ".rjust(4, " "), maximo, '\n'), AR_SALIDA)
        grabar_participacion_csv(apareo, AR_SALIDA, T_CLAVE, linea_max)
           
        apareo.close()
        max_ant = maximo
        apareo = open(t_apareo, 'r')
        maximo, linea_max = devolver_maximo_siguiente(apareo, POS_CLAVE, max_ant) 
