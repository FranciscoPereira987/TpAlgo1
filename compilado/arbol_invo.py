def rellenar_dict(archivo, diccionario):
    """
    [Autor:Augusto D'Avola ]
    [Ayuda:
    Rellena el diccionario de llamadas a funcion con 0
    en todas las funciones]
    """
    with open(archivo, 'r') as archivo_codigo:
        for linea in archivo_codigo:
            linea = linea.split(',')
            diccionario[linea[0]] = 0
    return

def buscar_funcion_principal(diccionario):
    """
    [Autor:Augusto D'Avola ]
    [Ayuda:
    Busca dentro del diccionario de llamadas a funcion
    aquella que no sea llamada nunca por otra funcion]
    """
    for elemento in diccionario.keys():
        if diccionario[elemento] == 0:
            return elemento

def _imprimir_arbol_invocacion(dict, cola):
    """
    [Autor:Augusto D'Avola ]
    [Ayuda: Imprime recursivamente los elementos de una cola
    de invocacion]
    """
    while cola:
        funcion = cola.pop(0)
        print(' --> {} ({})'.format(funcion, dict[funcion][0]),end='')
        _imprimir_arbol_invocacion(dict, dict[funcion][1])
    print('')
    print('                   ',end='')

def imprimir_arbol_invocacion(dict, funcion,nivel):
    """
    [Autor:Augusto D'Avola ]
    [Ayuda: Funcion encargada de imprimir un arbol de invocacion
    Pre: Dict es un diccionario con nombres de funcion como claves
    y tuplas de cantidad de lineas y cola de llamados como valor]
    """
    for i in range(nivel):
        print('                         ',end='')
    print('{} ({})'.format(funcion, dict[funcion][0]), end='')
    cola = dict[funcion][1]
    nivel = 0
    while cola:
        funcion = cola.pop(0)
        print(' --> ', end='')
        imprimir_arbol_invocacion(dict, funcion,nivel)
        nivel += 1
    print('')
    print('                 ',end='')

def imprimir(dict, funcion,nivel):
    print('\t' * nivel + "--> "+funcion + '  (' + str(dict[funcion][0]) + ')') 
    nivel += 1 
    cola = dict[funcion][1] 
    while cola: 
        funcion = cola.pop(0) 
        imprimir(dict, funcion, nivel) 


def arbol_invocacion():
    """
    [Autor:Augusto D'Avola ]
    [Ayuda: Funcion encargada de procesar e imprimir un
    arbol de invocacion]
    """
    dict = {} 
    dict_llamadas = {} 
    rellenar_dict('fuente_unico.csv',dict_llamadas) 
    with open('fuente_unico.csv', 'r') as archivo_codigo:
        for linea in archivo_codigo: 
            linea = linea.split(",")
            cola = [] 
            largo_funcion = len(linea)-3 
            for i in range(3,len(linea)):
                if linea[i].find(')') != -1: 
                    funcion = linea[i].strip().split('(') 
                    if funcion[0].find('.') != -1: 
                        funcion = funcion[0].split('.') 
                    else:
                        funcion = funcion[0].split(' ')
                    funcion = funcion[-1]
                    if funcion not in dict_llamadas: continue
                    cola.append(funcion)
                    dict_llamadas[funcion] += 1
            dict[linea[0]] = (largo_funcion,cola)
    funcion_principal = buscar_funcion_principal(dict_llamadas)
    imprimir(dict, funcion_principal,0)


