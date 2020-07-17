ARCHIVO_1 = "fuente_unico.csv"#"apareo_entra_01.txt"
ARCHIVO_2 = "comentarios.csv"#"apareo_entra_02.txt"
SALIDA = "apareo_salida.csv"

def grabar_csv(linea, archivo):
    archivo.write(",".join(linea) + '\n')


def aparear_csv(archivo_1, archivo_2, clave_1, clave_2):
    with open(ARCHIVO_1, "r") as archivo_1,\
            open(ARCHIVO_2, "r") as archivo_2,\
            open(SALIDA, "w") as salida:
                linea_ar_1 = archivo_1.readline().strip('\n').split(',')     
                linea_ar_2 = archivo_2.readline().strip('\n').split(',')     
                while linea_ar_1 != [''] and linea_ar_2 != ['']:
                    print(linea_ar_1)
                    print(linea_ar_2)
                    if linea_ar_1[clave_1] == linea_ar_2[clave_2]:
                        grabar_csv(linea_ar_1+linea_ar_2, salida) 
                        linea_ar_1 = archivo_1.readline().strip('\n').split(',')     
                        linea_ar_2 = archivo_2.readline().strip('\n').split(',')     
                    elif linea_ar_1[clave_1] > linea_ar_2[clave_2]:
                        linea_ar_2 = archivo_2.readline().strip('\n').split(',')     
                    elif linea_ar_1[clave_1] < linea_ar_2[clave_2]:
                        grabar_csv(linea_ar_1, salida) 
                        linea_ar_1 = archivo_1.readline().strip('\n').split(',')     
                 
                while linea_ar_1 != ['']:
                    grabar_csv(linea_ar_1, salida) 
                    linea_ar_1 = archivo_1.readline().strip('\n').split(',')     
    return SALIDA


#aparear_csv(ARCHIVO_1, ARCHIVO_2, 0, 0)
