SALIDA = "temporal_apareo.txt"


def grabar_csva(l_lineas, archivo):
    """
        [Autor: Ivan Coronel]
        [Ayuda: Recibe una lista con lineas correspondientes a
                dos archivos distintos y un manejador de archivos.
                Utiliza el manejador para grabar el archivo
                en formato csva.
    """
    for i in range(len(l_lineas) - 1 ):
        archivo.write(",".join(l_lineas[i]) + ';')
    archivo.write(",".join(l_lineas[-1]) + '\n')


def aparear_csv(t_archivo_1, t_archivo_2, clave_1, clave_2):
    """
        [Autor: Ivan Coronel]
        [Ayuda: Recibe el nombre de dos archivos csv y las
                posiciones de sus claves.
                Los procesa, graba un archivo con la informacion
                apareada y devuelve el nombre del archivo
                de salida y su cantidad de lineas.
    """
    grabados = 0
    with open(t_archivo_1, "r") as archivo_1,\
            open(t_archivo_2, "r") as archivo_2,\
            open(SALIDA, "w") as salida:
                linea_ar_1 = archivo_1.readline().strip('\n').split(',')     
                linea_ar_2 = archivo_2.readline().strip('\n').split(',')     
                while linea_ar_1 != [''] and linea_ar_2 != ['']:
                    if linea_ar_1[clave_1] == linea_ar_2[clave_2]:
                        grabar_csva([linea_ar_1, linea_ar_2], salida) 
                        linea_ar_1 = archivo_1.readline().strip('\n').split(',')     
                        linea_ar_2 = archivo_2.readline().strip('\n').split(',')     
                        grabados += 1
                        

                    elif linea_ar_1[clave_1] > linea_ar_2[clave_2]:
                        linea_ar_2 = archivo_2.readline().strip('\n').split(',')     
                    elif linea_ar_1[clave_1] < linea_ar_2[clave_2]:
                        grabar_csva([linea_ar_1, ['']] , salida) 
                        linea_ar_1 = archivo_1.readline().strip('\n').split(',')     
                        grabados += 1
                 
                while linea_ar_1 != ['']:
                    grabar_csva([linea_ar_1, ['']], salida) 
                    linea_ar_1 = archivo_1.readline().strip('\n').split(',')     
                    grabados += 1

    return SALIDA, grabados

