from info_participacion import *

#PRUEBA GRABAR PARTICIPACION.      - OK
#PRUEBA DEVOLVER MAXIMO SIGUIENTE. - OK

#Prueba_combinar_campos_lista - ok

#PRUEBA FORMATEAR CSVA - OK


def prueba_grabar_participacion():

    RUTA_PRUEBAS = "archivos_prueba/prueba_info/"


    with open(RUTA_PRUEBAS + "pruebaE01.csv", 'r') as ar_e01, \
            open(RUTA_PRUEBAS + "pruebaS02.txt", "w") as ar_s01:
                linea = ar_e01.readline()
                linea = ar_e01.readline()
                linea_max = linea.rstrip('\n').split(',')
                grabar_participacion_csv(ar_e01, ar_s01, T_CLAVE, linea_max)  


def prueba_devolver_maximo_sig():


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

def prueba_combinar_campos_lista():
    linea1, linea2 = "22,funcion_1,liNEas,asdf,sdfasd;22,funcion_1,liNEas,autor".rstrip('\n').split(';')
    l1 = linea1.split(',')
    l2 = linea2.split(',')
    print(combinar_campos_lista(l1, 2, len(linea1), ';'))
    print(combinar_campos_lista(l2, 3, len(linea2), ';'))


def prueba_formatear_csva():

    linea1 = "22,funcion_1,liNEas,asdf,sdfasd;22,funcion_1,liNEas,autor"
    print(formateo_csva(linea1))

#prueba_devolver_maximo_sig()
#prueba_combinar_campos_lista()

#prueba_formatear_csva()



informar_participacion()
