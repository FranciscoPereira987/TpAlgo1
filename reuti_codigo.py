import mezcla
import os
#----------------------Punto 3, analizador de reutilizacion de codigo-----------------------#


def leer_linea_archivo(archivo):
    """
    [Autor: Francisco Pereira]
    [Ayuda: como mezcla.leer_archivos se usa mucho de una forma especial aca
    decidi armar una funcion que lo haga, para que solamente aparezca una vez
    la forma rara de llamar a esa funcion en todo el codigo]
    """
    return mezcla.leer_archivos([archivo])[0]

def analizar_codigo(codigo, diccionario, nombre_funcion):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    Pre --> Ingresa el codigo de una funcion junto con su nombre
    Post --> Actualiza la cantidad de llamadas que hace esa funcion a otras
    funciones]
    """
    for linea in codigo:
            revisar_llamadas(diccionario, linea, nombre_funcion)

def generar_puntajes(archivo_codigo, diccionario):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    Pre --> Ingresan el archivo, la lista con los nombres de las funciones
    y el diccionario ya armado
    Post --> Devuelve los puntajes de cada una de las funciones segun la 
    tabla del enunciado del tp]
    """
    linea = leer_linea_archivo(archivo_codigo)

    while linea != ['']:
        funcion = f'{linea[2]}.{linea[0]}'
        analizar_codigo(linea[3:], diccionario, funcion)
        linea = leer_linea_archivo(archivo_codigo)



def revisar_llamadas(diccionario_funciones, linea, nombre_funcion_actual):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    Pre --> Ingresa el diccionario con el nombre de las funciones, el nombre de funcion actual
    y una linea de codigo de esta funcion
    Post --> Actualiza el valor de llamadas que hace la funcion en la linea
    de codigo que se pasa como parametro]
    """
    claves = list(diccionario_funciones.keys())
    indice = 1
    indice_punto = claves[0].find('.') + 1
    funcion = claves[0][indice_punto:]

    while (funcion not in linea) and indice < (len(claves)):
        indice_punto = claves[indice].find('.') + 1
        funcion = claves[indice][indice_punto:]
        indice += 1
        
    
    
    if funcion in linea:
        funcion = (claves[indice-1])
        diccionario_funciones[nombre_funcion_actual][funcion] += 1

def funciones_que_llaman(dicc_funciones):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    Pre --> Ingresa el dicc con las funciones y los puntajes
    Post --> Devuelve el dicc con x en donde una funcion es llamada por otra]
    """
    for funcion in dicc_funciones.keys():
        for funcion_que_llama in dicc_funciones.keys():
            valor = dicc_funciones[funcion_que_llama][funcion]
            if valor != 0 and valor != 'X':
                dicc_funciones[funcion][funcion_que_llama] = 'X'



def armar_lista(archivo_codigo):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    Pre --> Ingresa el archivo fuente_unico.csv
    Post --> Todas las funciones son puestas en una lista]
    """
    lista_funciones = []
    linea = leer_linea_archivo(archivo_codigo) 
                                                      
    while linea != ['']:
        funcion = f'{linea[2]}.{linea[0]}'
        if funcion not in lista_funciones:                                
            lista_funciones += [funcion]
        linea = leer_linea_archivo(archivo_codigo)

    archivo_codigo.seek(0)

    return lista_funciones

def generar_dicc_ceros(lista_funciones):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    pre ---> Ingresa una cantidad numerica entera
    Post ---> Devuelve una lista que tiene la cantidad de ceros que
    se paso como parametro]
    """
    dicc_ceros = {}
    for funcion in lista_funciones:
        dicc_ceros[funcion] = 0

    return dicc_ceros

def armar_diccionario(lista_funciones):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    Pre --> Ingresa la lista con el nombre de todas las funciones
    Post --> Devuelve un diccionario con formato:
                                            '<numero_funcion> - <Nombre_funcion>': <lista_ceros> 
            Donde lista_ceros es tan larga como funciones haya y tiene todos ceros]
    """
    
    diccionario = {} 
    for nombre_funcion in lista_funciones:
        diccionario[nombre_funcion] = generar_dicc_ceros(lista_funciones)
        

    return diccionario

def agregar_separador(texto):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    Pre--> Ingresa un texto cualquiera
    Post --> Busca el primer cambio de linea
    y le agrega al texto una linea de esa longitud 
    con _]
    """
    cantidad = texto.find('\n')
    texto += '_' * cantidad + '\n'

    return texto

def generar_fila_numerica(espacios_columna, a_escribir):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    Pre --> Ingresan la cantidad de espacios entre columna y columna
    y una lista que contiene los valores(numericos) a escribir en cada columna
    Post --> genera la fila, con separador | entre columnas
    ]
    """
    fila = ""
    for elemento in a_escribir:
        elemento = (espacios_columna//2) * ' ' + str(elemento)
        columna, texto_vacio = generar_texto_encolumnado(espacios_columna, elemento)
        fila += columna
        
    return fila + '\n'

def generar_texto_encolumnado(ancho_columna, texto):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    Pre --> Ingresa el ancho de la columna y el texto
    Post --> Devuelve una fila de texto y el resto del texto
    si es que no entra completamente en la columna
    ]
    """
    longitud_texto = len(texto)
    if longitud_texto > ancho_columna:
        columna = texto[:ancho_columna] + '|'
        texto = texto[ancho_columna:]
    else:
        espacios = " " * (ancho_columna - longitud_texto) + '|'
        columna = texto + espacios
        texto = ""
    
    return columna, texto

def generar_fila_total(texto, espacios_columna, valores_numericos):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    pre --> Ingresa el texto que va en la primera columna, los numeros de la fila
    y la cantidad de espacios por columna
    Post --> Devuelve texto, si es que resta algo y la fila en string
    ]
    """
    fila, texto = generar_texto_encolumnado(espacios_columna, texto)
    fila += generar_fila_numerica(espacios_columna // 4, valores_numericos)

    return fila, texto

def escribir_funcion(nombre_funcion, numero_funcion, dicc_funcion, espacios_columna, cant_filas):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    Ingresa la funcion y datos sobre el formato y llamadas de la misma
    Devuelve un string que representa a la "fila" de la funcion en 
    la impresion final]
    """
    valores_numericos = dicc_funcion.values()
    vacia = [' '] * len(valores_numericos) #Para las filas donde no haya que escribir numeros
    texto_funcion = f"{numero_funcion}-{nombre_funcion}" #a forma 1-main
    total = ""
    for i in range(cant_filas):

        if i >= (cant_filas // 2) and texto_funcion:
            fila, texto_funcion = generar_fila_total(texto_funcion, espacios_columna, valores_numericos)
            valores_numericos = vacia #Por si quedo texto de la funcion por escribir
            
        else:
            fila, texto_vacio = generar_fila_total('', espacios_columna, vacia)
            #Texto_vacio es una variable para evitar la tupla, no es de ninguna utilidad

        total += fila

    total = agregar_separador(total)

    return total
        
def escribir_primera_fila(cant_funciones, espacios_columna):

    numeros = list(range(1, cant_funciones + 1))
    vacia = [' '] * cant_funciones
    texto = ""
    fila, texto_vacio = generar_fila_total("", 20, vacia)
    texto += fila
    fila, texto_vacio = generar_fila_total("FUNCIONES", 20, numeros)
    texto += fila
    fila, texto_vacio = generar_fila_total("", 20, vacia)
    texto += fila

    texto = agregar_separador(texto)

    return texto

def escribir_archivo(dicc_funciones, espacios_columna, cant_filas):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    Genera el archivo analizador.txt e imprime la tabla en el mismo]
    """
    archivo = open("analizador.txt", 'w')
    i = 1
    fila_n = escribir_primera_fila(len(dicc_funciones), espacios_columna)
    for clave in dicc_funciones:
        archivo.write(fila_n)
        fila_n = escribir_funcion(clave, i, dicc_funciones[clave], espacios_columna, cant_filas)
        i += 1

    archivo.write(fila_n)
    archivo.close()

def generar_analizador():
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    En base a fuente_unico.csv genera el archivo
    analizador.txt y lo muestra en pantalla]
    """
    archivo_codigo = open('salida_codigo.csv', 'r')
    funciones = armar_lista(archivo_codigo)
    funciones = armar_diccionario(funciones)
    generar_puntajes(archivo_codigo, funciones)
    funciones_que_llaman(funciones)
    
    escribir_archivo(funciones, 20, 5)
    os.startfile('analizador.txt')

def main_reuti():
    archivo_codigo = open('salidaPrueba0.csv', 'r')
    lista_funciones = armar_lista(archivo_codigo)
    dicc_funciones = armar_diccionario(lista_funciones)
    archivo_codigo.seek(0)
    generar_puntajes(archivo_codigo, dicc_funciones)
    funciones_que_llaman(dicc_funciones)
    for funcion in dicc_funciones:
        print(funcion,'-->',dicc_funciones[funcion])
    archivo_codigo.close()
    escribir_archivo(dicc_funciones, 20, 3)
    
    
if __name__ == "__main__":
    generar_analizador()

