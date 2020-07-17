import apareo_csv

AR_FUENTE_UNICO = "fuente_unico.csv"
AR_COMENTARIOS  = "comentarios.csv"
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
INDICE_A = ["funcion_a", "instrucciones"]
POS_CLAVE = D_ENTRADA["autor"]
LONG_CAMPOS = 30
AR_SALIDA = "participacion.txt"
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
    maximo = ''
    linea_max = []
    linea = archivo.readline()
    while linea != '':
        clave = linea.rstrip('\n').split(',')[posicion_clave]
        if (clave < max_anterior and clave > maximo) \
                or (max_anterior == '' and  clave > maximo):
                    maximo = clave
                    linea_max = linea.rstrip('\n').split(',')
        linea = archivo.readline()
    return maximo, linea_max 
    

def grabar_participacion_csv(ar_entrada, ar_salida, clave, linea):
    """
        [AUTOR: Ivan Coronel]
        [AYUDA: Busca en el archivo de entrada los registros
        que coincidan en la posicion clave con el valor dado y los
        graba en el archivo de salida]
    """
    clave_valor = linea[D_ENTRADA[clave]]
    while linea != ['']:
        if linea[D_ENTRADA[clave]] == clave_valor:
            print(linea)
            info = seleccionar_campos_lista(linea, D_ENTRADA, INDICE_A)    
            print(info)
            ar_salida.write(
                    info[0].ljust(LONG_CAMPOS, ' ') 
                    + str(len(info[1].split(';')))
                    + '\n'
                    )

        linea = ar_entrada.readline().rstrip('\n').split(',')


def seleccionar_campos_lista(lista, diccionario, campos):
    """ [Autor: Ivan Coronel]
        [Ayuda: Recibe dos listas, lista contiene la informacion
        y campos contiene las posiciones a seleccionar.
        Se devuelve una lista que solo contendra los campos seleccionados.

    """
    return [lista[diccionario[campo]] for campo in campos]


def informar_participacion():
    grabar_encabezado()
    
    apareo = open(apareo_csv.aparea_csv(AR_FUENTE_UNICO, AR_COMENTARIOS, CLAVE_F_UNICO, CLAVE_COMENTARIOS), 'r')
    max_ant = ''
    maximo, linea_max = devolver_maximo_siguiente(apareo, POS_CLAVE, '') 
    apareo.close()
    apareo = open(apareo_csv.aparea_csv(AR_FUENTE_UNICO, AR_COMENTARIOS, 0, 0), 'r')
    while max_ant != maximo and maximo != '':
        salida.write("Autor: " + maximo +"\n\n")
        salida.write("Funcion".ljust(LONG_CAMPOS, ' ') 
                + "Lineas".ljust(LONG_CAMPOS, ' ') 
                + '\n')

        grabar_participacion_csv(apareo, AR_SALIDA, T_CLAVE, linea_max)
        apareo.close()
        apareo = open(apareo_csv.aparea_csv(AR_FUENTE_UNICO, AR_COMENTARIOS, CLAVE_F_UNICO, CLAVE_COMENTARIOS), 'r')
        maximo, linea_max = devolver_maximo_siguiente(apareo, POS_CLAVE, '') 



# ESPACIO PARA PRUEBAS.
## BORRAR TODO LO QUE HAY DEBAJO DE ESTA LINEA.


#PRUEBA GRABAR PARTICIPACION.   - OK
## GENERO ARCHIVO DE PRUEBA Y EJECUTO.
"""

RUTA_PRUEBAS = "archivos_prueba/prueba_info/"


with open(RUTA_PRUEBAS + "pruebaE01.csv", 'r') as ar_e01, \
        open(RUTA_PRUEBAS + "pruebaS02.txt", "w") as ar_s01:
            linea = ar_e01.readline()
            linea = ar_e01.readline()
            linea_max = linea.rstrip('\n').split(',')
            grabar_participacion_csv(ar_e01, ar_s01, T_CLAVE, linea_max)  

"""


#PRUEBA DEVOLVER MAXIMO SIGUIENTE

RUTA_PRUEBAS = "archivos_prueba/prueba_info/"
ar_e01 = open(RUTA_PRUEBAS + "pruebaE01.csv", 'r')

maximo, linea_max = devolver_maximo_siguiente(ar_e01, POS_CLAVE, '') 
print("LINEA MAX : " + str(linea_max))
print("MAXIMO    : " + str(maximo))
ar_e01.close()

for i in range(6):

    ar_e01 = open(RUTA_PRUEBAS + "pruebaE01.csv", 'r')
    print("MAXIMO    : " + str(maximo))
    print("LINEA MAX : " + str(linea_max))
    maximo, linea_max = devolver_maximo_siguiente(ar_e01, POS_CLAVE, maximo) 
    ar_e01.close()
