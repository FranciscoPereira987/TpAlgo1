import reuti_codigo

def armar_dicc_invocaciones():
    """
    [Autor: Francisco Pereira]
    [Ayuda: ]
    """
    funciones, lista_holder = reuti_codigo.generar_tabla()

    return funciones

def separar_multiples_llamadas(dicc_funciones):
    """
    [Autor: Francisco Pereira]
    [Ayuda: ]
    """
    claves = dicc_funciones.keys()
    for clave in claves:
        for llamada in claves:
            valor = dicc_funciones[clave][llamada]
            if valor != 'X':
                valor = int(valor)
                for i in range(1, valor):
                    dicc_funciones[clave][llamada] = int(dicc_funciones[clave][llamada]) - 1
                    asteriscos = '*' * i
                    dicc_funciones[clave][llamada + asteriscos] = 1
                    

def guardar_llamadas(dicc_funciones):
    """
    [Autor: Francisco Pereira]
    [Ayuda: ]
    """

    vacio = reuti_codigo.generar_dicc_ceros(dicc_funciones)
    lista_llamadas = reuti_codigo.contar_llamadas(dicc_funciones)
    indice = 0
    for clave in vacio:
        vacio[clave] = lista_llamadas[indice]
        indice += 1


    return vacio

def encontrar_funciones_no_llamadas(dicc_funciones):
    """
    [Autor: Francisco Pereira]
    [ayuda: ]
    """
    
    dicc_llamadas = guardar_llamadas(dicc_funciones)
    lista_no_llamadas = []
    for clave in dicc_llamadas:
        if dicc_llamadas[clave] == '0':
            lista_no_llamadas.append(clave)

    return lista_no_llamadas

def encontrar_claves(dicc_funciones, funcion):
    """
    [Autor: Francisco Pereira]
    [Ayuda: ]
    """
    claves = []
    
    for clave in dicc_funciones[funcion]:
        sin_as_clave = encontrar_asterisco(clave)
        sin_as_fun = encontrar_asterisco(funcion)
        valor = dicc_funciones[sin_as_fun][sin_as_clave]
        recursi = dicc_funciones[sin_as_clave][sin_as_fun]
        if valor != 'X' and valor > 0:
            claves.append(clave)
        elif valor == recursi and valor != 0:
            claves.append("recursiva")
    
    return claves

def armar_arbol(dicc_funciones, claves_funcion):
    """
    [Autor: Francisco Pereira]
    [Ayuda: ]
    """
    
    if claves_funcion:
        dicc = {}
        for clave in claves_funcion:
            if clave == 'recursiva':
                dicc[clave] = ""
            else:
                claves_clave = encontrar_claves(dicc_funciones, encontrar_asterisco(clave))
                dicc[clave] = armar_arbol(dicc_funciones, claves_clave)

    else:
        dicc = {}

    return dicc

def contar_cantidad(dicc, funcion):

    """
    [Autor: Francisco Pereira]
    [Ayuda: ]
    """
    if dicc[funcion] == {}:
        cantidad = 1
    else:
        cantidad = len(dicc)
        for clave in dicc[funcion]:
            cantidad += contar_cantidad(dicc[funcion], clave)
            
    
    return cantidad
    
def contar_lineas(nombre_funcion):
    """
    [Autor: Francisco Pereira]
    [Ayuda: ]
    """

    linea = reuti_codigo.encontrar_funcion(nombre_funcion)
    linea = linea[3:]

    cantidad_de_lineas = len(linea)

    return cantidad_de_lineas

def encontrar_asterisco(clave):
    """
    [Autor: Francisco Pereira]
    [Ayuda: ]
    """
    valor = clave.find('*') 
    if valor != -1:
        clave = clave[:valor]
    
    return clave

def asignar_lineas(dicc_funciones):
    """
    [Autor: Francisco Pereira]
    [Ayuda: ]
    """
    claves = dicc_funciones.keys()

    for clave in claves:
        if clave != 'lineas' and clave != 'recursiva':
            clave_i = encontrar_asterisco(clave)
            dicc_funciones[clave]['lineas'] = contar_lineas(clave_i)
            asignar_lineas(dicc_funciones[clave])

    


def encontrar_main(dicc_funciones):
    """
    [Autor: Francisco Pereira]
    [Ayuda: ]
    """
    no_llamadas = encontrar_funciones_no_llamadas(dicc_funciones)
    longitud_max = 0
    for clave in no_llamadas:
        claves_funcion = encontrar_claves(dicc_funciones, clave)
        arbol = {clave : armar_arbol(dicc_funciones, claves_funcion)}
        cant = contar_cantidad(arbol, clave)
        if cant > longitud_max:
            longitud_max = cant
            arbol_max = arbol
        

    return arbol_max


def imprimir_arbol(dicc_funciones, espacios, nombre, lineas, faltante):
    """
    [Autor: Francisco Pereira]
    [Ayuda: ]
    """
    funciones_que_llama = dicc_funciones.keys()
    texto = ""
    for clave in funciones_que_llama:
        
        if clave == 'recursiva':
            anadido = f'{nombre} ({lineas})'
            texto +=  "--->{:-<40}".format(anadido)
            
        else:
            lineas = dicc_funciones[clave].pop('lineas')
            sin_as = encontrar_asterisco(clave)
            anadido = f"{sin_as} ({lineas})"
            texto +=  "--->{:-<40}".format(anadido)
            faltante_propio = 40 - len(anadido)
            texto += imprimir_arbol(dicc_funciones[clave], espacios + 44, clave, lineas, faltante_propio)

        indice = len(texto) - texto[::-1].find(')')
        texto = texto[:indice]
        texto += '\n\n\n' + " " * (espacios - faltante) + faltante * "-"

    
    return texto


def arbol():
    """
    [Autor: Francisco Pereira]
    [Ayuda: ]
    """
    dicc = armar_dicc_invocaciones()
    separar_multiples_llamadas(dicc)
    arbol = encontrar_main(dicc)
    asignar_lineas(arbol)
    texto = imprimir_arbol(arbol, 0, "", 0, 0)
    archivo = open("arbolito.txt", 'w')
    archivo.write(4 * " " + texto[4:])
    archivo.close()
    
