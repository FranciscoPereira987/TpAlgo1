#Es un programa para separar lineas de codigo de comentarios


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
    
    if chr(35) in linea: #pregunto si hay comentario con #
        comentarios = comentarios + linea[linea.find(chr(35)):]
        linea = linea[:linea.find(chr(35))]
    
    # pregunto si es un comentario con triple dobles comillas en una linea
    elif linea.count("\"\"\"") == 2:
        comentarios = linea[linea.find("\"\"\""):]
        linea = linea[:linea.find("\"\"\"")]
        
    # pregunto si es un comentario con triple comillas simples en una linea
    elif linea.count("\'\'\'") == 2:
        comentarios = linea[linea.find("\'\'\'"):]
        linea = linea[:linea.find("\'\'\'")] +'\n'
    
    # pregunto si empieza un comentario multilinea con triple comillas dobles
    elif linea.count("\"\"\"") == 1:  
        comentado_multi = not comentado_multi  #Cambio el valor de comentado multi
        forma_de_comentar = "\"\"\""
    
    # pregunto si empieza un comentario multilinea con triple comillas simple
    elif linea.count("\'\'\'") == 1:
        comentado_multi = not comentado_multi  #Cambio el valor de comentado multi
        forma_de_comentar = "\'\'\'"
        
    return linea, comentado_multi, comentarios, forma_de_comentar

def leer_archivo(ruta_archivo):
    """[Autor: Claudio Gimenez]
       [Ayuda: Recibe un archivo y devuelve una lista de lineas de codigo
        y una lista de comentarios]
    """
    
    l_lineas = []
    l_comentarios = []
    archivo = open(ruta_archivo, 'r')
    comentado_multi = False
    linea, comentado_multi, comentarios, forma_de_comentar = leer_linea(archivo, comentado_multi)
    while linea or comentarios:
        if comentado_multi:
            comentarios = linea #si es una multinea la linea pasa a ser comentario
            linea = archivo.readline() 
            
            while forma_de_comentar  not in linea:
                comentarios = comentarios + linea # agrego linea a comentario
                linea = archivo.readline()
            comentarios = comentarios + linea # agrego la ultima '''  """
            comentado_multi = False # comentado multi pasa a False
            linea = '' 
        
        if linea.rstrip() != "": # agrego a lista la linea de codigo
            l_lineas.append(linea.strip('\n'))
            #print(linea, end = "")
        
        if comentarios != "": # agrego a la lista el comentario
            l_comentarios.append(comentarios.strip('\n'))
            #print(comentarios) 
        
        # leo otra linea
        linea, comentado_multi, comentarios, forma_de_comentar = leer_linea(archivo, comentado_multi)

    archivo.close()
    return l_lineas, l_comentarios # devuelvo las listas

def main():

    ruta = input("Ingrese la ruta a un archivo de python:\n")
    #print(leer_archivo(ruta))
    lineas, comentarios = leer_archivo(ruta)
    print("Estos son lineas de codigo")
    for i in lineas:
        print(i)
    print("Estos son comentarios")    
    for i in comentarios:
        print(i)
    print(lineas,comentarios)
    
if __name__ == "__main__":
    main()