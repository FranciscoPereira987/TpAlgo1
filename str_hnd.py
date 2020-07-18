import os


#--------------------Modulo que se encarga de procesar el texto obtenido de los archivos de python------------------#
def identificar_funciones(linea):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Pre --> Ingresa una linea de texto
           Post --> Devuelve True si en esa linea se define una funcion
           False en caso contrario]
    """

    return "def " in linea

def nombre_funcion(linea):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Pre --> Ingresa una linea donde se declara una funcion
           Post --> Devuelve el nombre de la funcion]
    """
    indice_max = linea.find("(")
    indice_min = linea.find(" ") + 1
    nombre = linea[indice_min:indice_max]

    return nombre

def identificar_alfabeticamente(nombre_actual, nombre_maximo, nombre_minimo):
    """
    [Autor: Francisco Pereira]
    [Ayudo: Pre --> Ingresan los nombres de funciones (el actual, el maximo y el minimo)
           Post --> Devuelve True si hay cambios False en caso contrario]
    """
    
    return nombre_actual < nombre_maximo and nombre_actual > nombre_minimo

def devolver_parametros(linea):
    """
    [Autor: Francisco Pereira]
   [Ayuda:
    Pre --> Ingresa una linea de codigo donde se define una funcion
    Post --> Devuelve los parametros formales separados por /]
    """
    indice_inicio = linea.find('(')
    ultimo_indice = linea.find(')') + 1

    parametros = procesar_comas(linea[indice_inicio:ultimo_indice])
    
    
    return parametros

def nombre_modulo(linea):
    """
    [Autor: Francisco]
    [Ayuda:
    Pre --> Ingresa una linea donde se encuentra la ruta a un archivo de python
    Post --> Devuelve el nombre del archivo de python]
    """
    ultimo_indice = linea.find(".py")
    if os.name == "nt":
        primer_indice = len(linea) - linea[::-1].find("\\")
    else:
        primer_indice = len(linea) - linea[::-1].find("/")
        
    return linea[primer_indice:ultimo_indice]

def lista_a_string(l_codigo, l_comentarios):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Le ingresan dos listas, separa los campos por comas]
    """
    str_codigo = ','.join(l_codigo)
    str_comentarios = ','.join(l_comentarios)

    return str_codigo, str_comentarios


def procesar_comas(texto):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Saca todas las comas que puedan aparecen en comentarios
    y en el codigo y las cambia por /]
    """
    texto = texto.replace(',', '/')

    return texto

def procesar_codigo(l_codigo):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    Pre ---> Ingresa la lista que posee el codigo de una funcion de python
    Post ---> Devuelve la lista, habiendo reemplazado las comas que pudiesen haber aparecido 
    ]
    """
    for i in range(0, len(l_codigo)):
        l_codigo[i] = procesar_comas(l_codigo[i])
    
def procesar_comentarios(l_comentarios):
    """
    [Autor: Francisco Pereira]
    [Ayuda:
    pre --> Ingresa la lista que contiene los comentarios de una funcion
    Post --> Devuelve los comentarios formateados segun el formato pedido
    ]
    """
    l_comentarios[0] = procesar_multilinea(l_comentarios[0])
    for i in range(1, len(l_comentarios)):
        l_comentarios[i] = procesar_comas(l_comentarios[i])


def separar_campo(comentario, campo):
    """
    [Autor: Francisco Pereira]
    [Ayuda: 
    Pre --> Ingresa el comentario multilinea
    Post --> Devuelve el string que le sigue al campo hasta ]
    si no esta devuelve un string vacio]
    """
    if campo not in comentario.lower():
        devolver = ''

    else:
        indice_inicio = (comentario.lower()).find(campo)
        indice_final = indice_inicio + (comentario[indice_inicio:]).find(']')
        devolver = comentario[indice_inicio:indice_final]

    return devolver

def procesar_multilinea(comentario):
    """
    [Autor: Francisco Pereira]
    [Ayuda: 
    pre --> Ingresa el comentario multilinea del principio
    Post --> Devuelve el autor y ayuda si estan, si no es multilinea
    devuelve dos campos vacios y el comentario
    si no, devuelve dos campos vacios]
    """
    comentario = comentario.replace('\n', "")
    autor = procesar_comas(separar_campo(comentario, 'autor'))
    ayuda = procesar_comas(separar_campo(comentario, 'ayuda'))
    if autor or ayuda:
        campos = f'{autor},{ayuda},'
    else:
        
        campos = ",,"

    return campos


def procesar_funcion(l_codigo, l_comentarios):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Procesa el codigo y comentario de una fucion
    devolviendolo en el formato correrspondiente para
    fuente_unico y comentarios]
    """
    if l_codigo:
        procesar_codigo(l_codigo)
    if l_comentarios:
        procesar_comentarios(l_comentarios)
    elif not l_comentarios:
        l_comentarios = ['', '', '']
    codigo, comentarios = lista_a_string(l_codigo, l_comentarios)

    return codigo, comentarios
