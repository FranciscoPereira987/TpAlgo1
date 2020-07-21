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
        funcion = f'{linea[0]}.{linea[2]}'
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
    indice = 0
    funcion = "zzzzzzzzzzzzzzz"

    for clave in claves:
        indice_punto = clave.find('.') 
        funcion = clave[:indice_punto] + '('
        if funcion in linea:
            funcion = clave
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

def encontrar_funcion(nombre_funcion):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Encuentra la linea de un archivo donde aparece una funcion
    pasada como parametro]
    """
    archivo = open("fuente_unico.csv", 'r')
    funcion_modulo = linea = "Esto no es una linea ni una funcion"
    
    while funcion_modulo != nombre_funcion and linea:
        linea = leer_linea_archivo(archivo)
        funcion_modulo = f"{linea[0]}.{linea[2]}"
    
    archivo.close()
    return linea

def contar_recursiva(nombre_funcion):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Cuenta la cantidad de veces
    que una funcion con recursividad directa se llama
    a si misma.]
    """
    
    cantidad = 0
    linea = encontrar_funcion(nombre_funcion)
    funcion_modulo = f"{linea[0]}.{linea[2]}"
    
    if funcion_modulo == nombre_funcion:
        funcion = linea[0]
        codigo = linea[3:]
        cantidad = (','.join(codigo)).count(funcion)

    
    return cantidad

def contar_llamadas(dicc_funciones):
    """
    [Autor: Francisco Pereira]
    [Ayuda: cuenta la cantidad de veces que cada funcion fue llamada por otras
    y lo guarda en una lista, con la cantidad por funcion]
    """
    indice = 0
    lista_llamadas = [0] * len(dicc_funciones)
    for funcion in dicc_funciones.keys():
        for funcion_que_llama in dicc_funciones.keys():
            valor = dicc_funciones[funcion][funcion_que_llama]
            espejo = dicc_funciones[funcion_que_llama][funcion]
            if valor == 'X' \
                and espejo != 'X': #Para evitar errores si hay 
                #recursividad
                lista_llamadas[indice] += int(dicc_funciones[funcion_que_llama][funcion])
                
            elif valor == 'X': #Aca van a entrar funciones recursivas
                #Solo se soportan funciones con recursividad directa 
                lista_llamadas[indice] += contar_recursiva(funcion)

        lista_llamadas[indice] = str(lista_llamadas[indice])
        indice += 1

    return lista_llamadas

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
        funcion = f'{linea[0]}.{linea[2]}'
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
        if elemento == 0:
            elemento = ' '
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
        
def generar_primera_fila(cant_funciones, espacios_columna):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Tomando la cantidad de funciones
    genera la primera fila del archivo analizador.txt]
    """
    numeros = list(range(1, cant_funciones + 1))
    vacia = [' '] * cant_funciones
    texto = ""
    lista = [
    ("", espacios_columna, vacia),
    ("FUNCIONES", espacios_columna, numeros), 
    ("", espacios_columna, vacia)
    ]

    for parametros in lista:

        fila, texto_vacio = generar_fila_total(*parametros)
        texto += fila
    
    texto = agregar_separador(texto)

    return texto

def generar_ultima_fila(dicc_funciones, espacios_columna, cant_filas):
    """
    [Autor: Francisco Pereira]
    [Ayuda: genera el string de la ultima fila
    del archivo analizador.txt]
    """
    fila, texto  = generar_texto_encolumnado(espacios_columna, "Total invocaciones")
    while texto:
        a_agregar, texto = generar_texto_encolumnado(espacios_columna, texto)
        fila += a_agregar

    lista_llamadas = contar_llamadas(dicc_funciones)
    fila += generar_fila_numerica(espacios_columna // 4, lista_llamadas)

    fila = agregar_separador(fila)

    return fila

def escribir_archivo(dicc_funciones, espacios_columna, cant_filas):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    Genera el archivo analizador.txt e imprime la tabla en el mismo]
    """
    archivo = open("analizador.txt", 'w')
    i = 1
    fila_1 = generar_primera_fila(len(dicc_funciones), espacios_columna)
    ultima = generar_ultima_fila(dicc_funciones, espacios_columna, cant_filas)
    archivo.write(fila_1 + ultima)

    for clave in dicc_funciones:
        
        fila_n = escribir_funcion(clave, i, dicc_funciones[clave], espacios_columna, cant_filas)
        archivo.write(fila_n)
        i += 1
    
    archivo.close()

def generar_tabla():
    """
    [Autor: Francisco Pereira]
    [Ayuda: Genera el diccionario con los datos a imprimir
    en el archivo analizador
    ]
    """
    with open('fuente_unico.csv', 'r') as archivo_codigo:
    
        funciones = armar_lista(archivo_codigo)
        funciones = armar_diccionario(funciones)
        generar_puntajes(archivo_codigo, funciones)
        linea_ultima = contar_llamadas(funciones)
        funciones_que_llaman(funciones)

    return funciones, linea_ultima

def generar_analizador():
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    En base a fuente_unico.csv genera el archivo
    analizador.txt y lo muestra en pantalla]
    """
    funciones, linea_ultima = generar_tabla()
    
    escribir_archivo(funciones, 20, 5)
    imprimir_resultados("analizador.txt")

def imprimir_resultados(nombre_archivo):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Trata de imprimir los resultados
    Si no se esta en windows, trata de usar geany
    en caso contrario lo imprime, por pantalla]
    """
    if os.name == 'nt':
        os.startfile(nombre_archivo)
    else:
        try:
            os.system(f'geany {nombre_archivo}')
        except:
            archivo = open(nombre_archivo, 'r')
            linea = "   "
            while linea:
                linea = archivo.readline()
                print(linea, end = "")
            archivo.close()
    
if __name__ == "__main__":
    generar_analizador()

