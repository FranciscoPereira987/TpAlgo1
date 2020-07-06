import mezcla
#----------------------Punto 3, analizador de reutilizacion de codigo-----------------------#
def leer_linea_archivo(archivo):
    """
    Autor: Francisco
    Ayuda: como mezcla.leer_archivos se usa mucho de una forma especial aca
    decidi armar una funcion que lo haga, para que solamente aparezca una vez
    la forma rara de llamar a esa funcion en todo el codigo
    """
    return mezcla.leer_archivos([archivo])[0]

def armar_lista(archivo_codigo):
    """
    Autor: Francisco Pereira
    Ayuda:
    Pre --> Ingresa el archivo fuente_unico.csv
    Post --> Todas las funciones son puestas en una lista
    """
    lista_funciones = []
    linea = leer_linea_archivo(archivo_codigo) 
                                                      
    while linea != ['']:                                
        lista_funciones += [linea[0]]
        linea = leer_linea_archivo(archivo_codigo)

    return lista_funciones

def generar_dicc_ceros(lista_funciones):
    """
    Autor: Francisco Pereira
    Ayuda:
    pre ---> Ingresa una cantidad numerica entera
    Post ---> Devuelve una lista que tiene la cantidad de ceros que
    se paso como parametro
    """
    dicc_ceros = {}
    for funcion in lista_funciones:
        dicc_ceros[funcion] = 0

    return dicc_ceros

def armar_diccionario(lista_funciones):
    """
    Autor: Francisco Pereira
    Ayuda:
    Pre --> Ingresa la lista con el nombre de todas las funciones
    Post --> Devuelve un diccionario con formato:
                                            '<numero_funcion> - <Nombre_funcion>': <lista_ceros> 
            Donde lista_ceros es tan larga como funciones haya y tiene todos ceros
    """
    
    diccionario = {}
    for nombre_funcion in lista_funciones:
        diccionario[nombre_funcion] = generar_dicc_ceros(lista_funciones)
        

    return diccionario

def revisar_llamadas(diccionario_funciones, linea, nombre_funcion_actual):
    """
    Autor: Francisco Pereira
    Ayuda:
    Pre --> Ingresa el diccionario con el nombre de las funciones, el nombre de funcion actual
    y una linea de codigo de esta funcion
    Post --> Actualiza el valor de llamadas que hace la funcion en la linea
    de codigo que se pasa como parametro
    """
    claves = list(diccionario_funciones.keys())
    funcion = claves.pop(0)

    while (funcion not in linea) and claves:
        funcion = claves.pop(0)
    
    if funcion in linea:
        diccionario_funciones[nombre_funcion_actual][funcion] += 1

def funciones_que_llaman(dicc_funciones):
    """
    Autor: Francisco Pereira
    Ayuda:
    Pre --> Ingresa el dicc con las funciones y los puntajes
    Post --> Devuelve el dicc con x en donde una funcion es llamada por otra
    """
    for funcion in dicc_funciones.keys():
        for funcion_que_llama in dicc_funciones.keys():
            valor = dicc_funciones[funcion_que_llama][funcion]
            if valor != 0 and valor != 'X':
                dicc_funciones[funcion][funcion_que_llama] = 'X'
    

def analizar_codigo(codigo, diccionario, nombre_funcion):
    """
    Autor: Francisco
    Ayuda:
    Pre --> Ingresa el codigo de una funcion junto con su nombre
    Post --> Actualiza la cantidad de llamadas que hace esa funcion a otras
    funciones
    """
    for linea in codigo:
            revisar_llamadas(diccionario, linea, nombre_funcion)

def generar_puntajes(archivo_codigo, diccionario):
    """
    Autor: Francisco
    Ayuda:
    Pre --> Ingresan el archivo, la lista con los nombres de las funciones
    y el diccionario ya armado
    Post --> Devuelve los puntajes de cada una de las funciones segun la 
    tabla del enunciado del tp
    """
    linea = leer_linea_archivo(archivo_codigo)

    while linea != ['']:
        analizar_codigo(linea[3:], diccionario, linea[0])
        linea = leer_linea_archivo(archivo_codigo)
    
def main():
    archivo_codigo = open('salidaPrueba1.csv', 'r')
    lista_funciones = armar_lista(archivo_codigo)
    dicc_funciones = armar_diccionario(lista_funciones)
    archivo_codigo.seek(0)
    generar_puntajes(archivo_codigo, dicc_funciones)
    funciones_que_llaman(dicc_funciones)
    for funcion in dicc_funciones:
        print(funcion,'-->',dicc_funciones[funcion])
    archivo_codigo.close()
    
if __name__ == "__main__":
    main()