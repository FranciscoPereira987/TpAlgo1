

def rellenar_dict(archivo, diccionario):
    """
    [Autor: Augusto D'Avola ]
    [Ayuda: Rellena el diccionario de llamadas a funcion con 0
    en todas las funciones]
    """
    with open(archivo, 'r') as archivo_codigo:
        for linea in archivo_codigo:
            linea = linea.split(',')
            diccionario[linea[0]] = 0
    return

def buscar_funcion_principal(diccionario):
    """
    [Autor: Augusto D'Avola ]
    [Ayuda: Busca dentro del diccionario de llamadas a funcion
    aquella que no sea llamada nunca por otra funcion]
    """
    llaves = diccionario.keys()
    lista = []
    for clave in llaves:
        if diccionario[clave] == 0:
            lista.append(clave)

    main = determinar_main(lista)

    return main

def determinar_main(lista):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Si hay mas de una funcion
    le da la chance al usuario de que defina
    el main]
    """
    if len(lista) == 1:
        eleccion = lista.pop()
    else:
        print("Elija la funcion principal")
        imprimir_elementos(lista)
        eleccion = ""
        while eleccion not in lista:
            eleccion = input(">>>")
    
    return eleccion


def imprimir_elementos(lista):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Imprime todas las funciones que no son llamadas]
    """
    for elemento in lista:
        print(elemento, end = "  ")
    print("")

def imprimir(dict, funcion,nivel):
    """
    [Autor: Augusto D'Avola ]
    [Ayuda: Funcion encargada de imprimir un arbol de invocacion
    con su nivel y llamado a la funcion correspondiente,
    Dict es un diccionario con nombres de funcion como claves
    y tuplas de cantidad de lineas y cola de llamados como valor]
    """
    print('\t' * nivel + "--> "+funcion + '  (' + str(dict[funcion][0]) + ')')
    nivel += 1
    cola = dict[funcion][1]
    while cola:
        funcion = cola.pop(0)
        imprimir(dict, funcion, nivel)

def procesar_linea(linea,dict, dict_llamadas):
    """
    [Autor: Augusto D'Avola ]
    [Ayuda: Recibe una lista con el contenido de una linea del csv,
    el diccionario de invocacion y el diccionario de llamadas,
    procesa la linea y actualiza los valores en el diccionario]
    """
    cola = []
    largo_funcion = len(linea) - 3
    for i in range(3,len(linea)):
        if linea[i].find(')') != -1:
            posibles_funciones = linea[i].strip().split('(')
            for funcion in posibles_funciones:
                if funcion.find('.') != -1:
                    funcion = funcion.split('.')
                else:
                    funcion = funcion.split(' ')
                if funcion[-1] in dict_llamadas:
                    cola.append(funcion[-1])
                    dict_llamadas[funcion[-1]] += 1
    dict[linea[0]] = (largo_funcion,cola)


def arbol_invocacion():
    """
    [Autor: Augusto D'Avola ]
    [Ayuda: Funcion encargada de procesar e imprimir un
    arbol de invocacion]
    """
    dict = {}
    dict_llamadas = {}
    rellenar_dict('fuente_unico.csv',dict_llamadas)
    with open('fuente_unico.csv', 'r') as archivo_codigo:
        for linea in archivo_codigo:
            linea = linea.split(",")
            procesar_linea(linea, dict, dict_llamadas)
    funcion_principal = buscar_funcion_principal(dict_llamadas)
    imprimir(dict, funcion_principal,0)
