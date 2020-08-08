#Es un programa para separar lineas de codigo de comentarios
import str_hnd

def leer_linea(archivo, comentado_multi):
    """[Autor: Claudio Gimenez]
       [Ayuda: Lee una linea del archivo que recibe como parametro,  
        devuele linea, comentarios o si es un comentario multlinea
        y forma de coementar si es multilinea]
    """
    linea = archivo.readline()
    
    linea, comentado_multi, comentarios, forma_de_comentar = \
    identificar_comentarios(linea, comentado_multi)
    
    return linea, comentado_multi, comentarios, forma_de_comentar

def identificar_comentarios(linea, comentado_multi):
    """[Autor: Claudio Gimenez]
       [Ayuda: Identifica si hay comentarios en la linea que recibe,  
        como parametro, tambien recibe comentado_multi en False que 
        si es multilinea lo devuelvo en True, devuelve comentarios,
        lineay forma de comentar en multilinea si es "" o '']
    """
    comentarios = ''
    forma_de_comentar = ''
    numeral = chr(35)
    
    if numeral in linea: #pregunto si hay comentario con #
        comentarios = comentarios + linea[linea.find(numeral) + 1:]
        linea = linea[:linea.find(numeral)]
    
    # pregunto si empieza un comentario multilinea con triple comillas dobles
    elif linea.count("\"\"\"") == 1:  
        comentado_multi = not comentado_multi  #Cambio el valor de comentado multi
        forma_de_comentar = "\"\"\""
    
    # pregunto si empieza un comentario multilinea con triple comillas simple
    elif linea.count("\'\'\'") == 1:
        comentado_multi = not comentado_multi  #Cambio el valor de comentado multi
        forma_de_comentar = "\'\'\'"
        
    return linea, comentado_multi, comentarios, forma_de_comentar

def sin_indentacion(linea):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Identifica si una linea de codigo
    contra el margen izquierdo, empieza o no, con def
    o ' ']
    """
    inicio = False
    if linea:
        inicio = linea[0].isalpha()
        #Por que, los espacios, newlines y tabs, dan falso
    return inicio

def fin_funcion(linea):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Devuelve verdadero si se llego al final de una funcion
    o al final de la declaracion de funciones]
    """
    no_indent = sin_indentacion(linea)

    return no_indent

def leer_funcion(archivo):
    """[Autor: Claudio Gimenez]
       [Ayuda: Recibe un archivo y devuelve una lista de lineas de codigo
        y una lista de comentarios]
    """
    
    l_lineas = []
    l_comentarios = []
    comentado_multi = False #luego lo uso para validar si es una multilinea
    fin = False
    linea, comentado_multi, comentarios, forma_de_comentar = leer_linea(archivo, comentado_multi)
    while not fin and linea:

        if linea.rstrip() != "" and not comentado_multi: # agrego a lista la linea de codigo
            l_lineas.append(linea.strip('\n'))
            #print(linea, end = "")

        elif comentado_multi:
            comentarios = linea #si es una multinea la linea pasa a ser comentario
            linea = archivo.readline() 
            
            while forma_de_comentar  not in linea:
                comentarios = comentarios + linea # agrego linea a comentario
                linea = archivo.readline()
                linea = linea.rstrip('\n')
            comentarios = comentarios + linea # agrego la ultima '''  """
            comentado_multi = False # comentado multi pasa a False
            #linea = '' 
        
        if comentarios != "": # agrego a la lista el comentario
            l_comentarios.append(comentarios.strip('\n'))
            #print(comentarios) 
        
        # leo otra linea
        linea, comentado_multi, comentarios, forma_de_comentar = leer_linea(archivo, comentado_multi)
        fin = fin_funcion(linea)
    
    if "return " in linea:
        l_lineas.append(linea.strip('\n'))
        
    return linea, l_lineas, l_comentarios # devuelvo las listas

def main_sep():

    ruta = input("Ingrese la ruta a un archivo de python:\n")
    #print(leer_archivo(ruta))
    linea, lineas, comentarios = leer_funcion(ruta)
    print("Estos son lineas de codigo")
    for i in lineas:
        print(i)
    print("Estos son comentarios")    
    for i in comentarios:
        print(i)
    print(lineas,comentarios)
    
if __name__ == "__main__":
    main_sep()
