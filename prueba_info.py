from info_participacion import *

#PRUEBA GRABAR PARTICIPACION.      - OK
#PRUEBA DEVOLVER MAXIMO SIGUIENTE. - OK

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


prueba_devolver_maximo_sig()
