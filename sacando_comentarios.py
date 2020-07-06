#Es una mejora a leyendo_while


def leer_linea(archivo, comentado_multi):

    linea = archivo.readline()
    linea, comentado_multi = identificar_comentarios(linea, comentado_multi)
    if comentado_multi:
        linea = " "

    return linea, comentado_multi

def identificar_comentarios(linea, comentado_multi):

    if "#" in linea:
        linea = linea[:linea.find("#")] + "\n"
    elif "\"\"\"" in linea:
        if linea.count('\"\"\"') == 2:
            linea = linea[:linea.find('\"\"\"')] +'\n'
        else:
            comentado_multi = not comentado_multi  #Cambio el valor de comentado multi

    """ Hola esto es un multilinea en una linea"""

    return linea, comentado_multi

def leer_archivo(ruta_archivo):
    
    archivo = open(ruta_archivo, 'r')
    comentado_multi = False
    linea, comentado_multi = leer_linea(archivo, comentado_multi)
    while linea:
        print(linea, end = "")
        linea, comentado_multi = leer_linea(archivo, comentado_multi)

    archivo.close()

def main():

    ruta = input("Ingrese la ruta a un archivo de python:\n")
    leer_archivo(ruta)

if __name__ == "__main__":
    main()