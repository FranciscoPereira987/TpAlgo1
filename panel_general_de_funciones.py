import reuti_codigo
import csv


def armar_lista_parametros(archivo_codigo):
    """
    [Autor: Nicolas Valenzuela]
    [Ayuda: Recibe el archivo csv, arma una lista con la cantidad de parametros y devuelve la lista armada con la cantidad de parametros por funcion]
    """
    lista_funciones =  []
    linea =  reuti_codigo.leer_linea_archivo(archivo_codigo) 
                                                      
    while linea !=  ['']:
        funcion =  f'{linea[1]}'
        x= funcion.count('/')    

        if x > 0 :
            lista_funciones.append(x+1)
        elif len(funcion) > 2 :
                lista_funciones.append(1)
        else:
                lista_funciones.append(x)

        linea =  reuti_codigo.leer_linea_archivo(archivo_codigo)

    archivo_codigo.seek(0)

    return lista_funciones

def cantidad_de_lineas():
    """
    [Autor: Nicolas Valenzuela]
    [Ayuda: Arma una lista con la cantidad de lineas y devuelve la lista armada con la cantidad de lineas por funcion]
    """
    archivo_codigo =  open('fuente_unico.csv','r')  
    palabra =  ','   
    ocurrencias =  []
    for lineas in archivo_codigo:
            if palabra in lineas :
                x =  lineas.count(palabra)                
                ocurrencias.append(x-2)
            else:
                ocurrencias.append(0)
    archivo_codigo.close()            
    return ocurrencias
def lineas_cod(archivo):
    """
    [Autor: Nicolas Valenzuela]
    [Ayuda: Recibe el archivo fuente unico y guarda los nombres de las funciones en una lista devolviendo la misma]
    """
    lista_lineas =  []
    linea =  reuti_codigo.leer_linea_archivo(archivo) 
                                                      
    while linea !=  ['']:
        funcion =  f'{linea[0]}'
                                       
        lista_lineas +=  [funcion]
        linea =  reuti_codigo.leer_linea_archivo(archivo)

    archivo.seek(0)

    return lista_lineas


def lista_ayuda():
    """
    [Autor: Nicolas Valenzuela]
    [Ayuda: Busca si las funciones tiene ayuda y devuelve la lista armada con si o no dependiendo la respuesta]
    """
    archivo_codigo= open('comentarios.csv','r')   
    l_respuesta =  []
    linea =  reuti_codigo.leer_linea_archivo(archivo_codigo) 
    while linea !=  ['']:
        if linea[2] !=  '' :
            l_respuesta.append('Si')
        else:
            l_respuesta.append('No')                                              
        linea =  reuti_codigo.leer_linea_archivo(archivo_codigo)
    archivo_codigo.seek(0)
    return l_respuesta
def funcion_autor():
    """
    [Autor: Nicolas Valenzuela]
    [Ayuda: Busca autores de funcion y devuelve una lista con sus respectivos nombres]
    """
    archivo_codigo =  open('comentarios.csv','r') 
    lista_autores =  []
    linea =  reuti_codigo.leer_linea_archivo(archivo_codigo) 
                                                      
    while linea !=  ['']:
        funcion =  f'{linea[1]}'
        if 'utor' or 'UTOR' in funcion :
            if ':' in funcion:
                lista_autores +=  [funcion[6:]]
            else:
                lista_autores +=  [funcion[5:]]
        else:
            lista_autores +=  [funcion]
        linea =  reuti_codigo.leer_linea_archivo(archivo_codigo)

    
    return lista_autores

def comentarios_extra():
    """
    [Autor: Nicolas Valenzuela]
    [Ayuda: Busca si hay comentarios extra aparte de ayuda autor y devuelve una lista con la cantidad de lineas extra]
    """
    archivo_codigo= open('comentarios.csv','r') 
    lista_extra= []
    for row in archivo_codigo:
        x=  row.count(',')
        
        if x > 2:
            x =  x -2
            lista_extra.append(x)
        else:
            lista_extra.append(0)
    return(lista_extra)
def invocaciones_():
    """
    [Autor: Nicolas Valenzuela]
    [Ayuda: Busca la cantidad de veces que se uso cada funcion y devuelve todo en una lista]
    """
    archivo= open('fuente_unico.csv','r') 
    funciones= (lineas_cod(archivo))  
    final= []
    for r in range(len(funciones)):
        total= []
        total =  cantidad_de([funciones[r]+'('])
        x=  0
        for i in total:
            x =  x + i
        final.append(x)
    return final

def cantidad_de(palabras):
    """
    [Autor: Nicolas Valenzuela]
    [Ayuda: Recibe una lista de palabras ( o palabra ) y busca cuantas veces se repite por cada funcion enviando una lista con el resultado]
    """
    archivo_codigo= open('fuente_unico.csv','r') 
    ocurrencias =  []
    
    for row in archivo_codigo:
        x= 0
        for palabra in palabras:
            if palabra in row:
                x =  x + row.count('   '+palabra)
                
        ocurrencias.append(x)
            
    return ocurrencias


def crear_csv():
    """
    [Autor: Nicolas Valenzuela]
    [Ayuda: Crea archivo panel_general.csv y guarda sus respectivos datos en los campos]
    """
    archivo_codigo =  open('fuente_unico.csv','r') 
    funciones =  reuti_codigo.armar_lista(archivo_codigo)
    parametr =  armar_lista_parametros(archivo_codigo)    
    cant_lineas =  cantidad_de_lineas()
    cant_return = cantidad_de([' return '])        
    cant_if = cantidad_de([' if ',' elif '])
    cant_for = cantidad_de([' for '])
    cant_while = cantidad_de([' while '])
    cant_break = cantidad_de([' break '])
    cant_exit = cantidad_de([' exit '])   
    c_invoca = invocaciones_()
    ayuda = lista_ayuda()
    autores = funcion_autor()
    coment_extra = comentarios_extra()
    
    with open('panel_general.csv', 'w', newline= '') as miarchivo:
        parametros =  ['FUNCION','Parámetros','Líneas','Invocaciones','Returns','if/elif','for','while','break','Exit','Coment','Ayuda','Autor']
        escribir =  csv.DictWriter(miarchivo, fieldnames= parametros)
        escribir.writeheader()
        for i in range(len(funciones) ):
            
            escribir.writerow({'FUNCION': funciones[i], 'Parámetros' : parametr[i], 'Líneas' : cant_lineas[i], 'Invocaciones' : c_invoca[i], 'Returns': cant_return[i], 'if/elif' : cant_if[i],
                               'for' : cant_for[i], 'while' : cant_while[i], 'break' : cant_break[i], 'Exit' : cant_exit[i],
                               'Coment' : coment_extra[i], 'Ayuda' : ayuda[i], 'Autor' : autores[i]})
            
        archivo_codigo.close
        return ()

def listar_(i):
    """
    [Autor: Nicolas Valenzuela]
    [Ayuda: Recibe la columna a imprimir y devuelve una lista con todos los parametros de la dicha columna]
    """
    archivo_codigo =  open('panel_general.csv','r')
    lista_ =  []
    linea =  reuti_codigo.leer_linea_archivo(archivo_codigo) 
                                                      
    while linea !=  ['']:
        funcion =  f'{linea[i]}'                                    
        lista_ +=  [funcion]
        linea =  reuti_codigo.leer_linea_archivo(archivo_codigo)

    archivo_codigo.seek(0)
    archivo_codigo.close
    
    return lista_

def encolumnar(texto):
    """
    [Autor: Nicolas Valenzuela]
    [Ayuda: Recibe lista y devuelve la lista con espacios y el | ya listo para imprimir]
    """
    ancho = 0
    espacios = " "
    for i in range(len(texto)):
        if ancho < len (texto[i]):
            ancho = len(texto[i]) + 2
    for g in range(len(texto)):       
        if len(texto[g]) < ancho:           
            espacios = " " *( ancho - len(texto[g]))            
            texto[g] = (texto[g] + espacios + '|')
    return texto

def listar_todos():
    """
    [Autor: Nicolas Valenzuela]
    [Ayuda: Cicla para hacer una lista juntando todos los valores a encolumnar]
    """
    lista = []
    for j in range(13):
        columna = listar_(j)
        columnas = encolumnar(columna)
        lista.append(columnas)
    lista2 = []
    while len(lista[0])>len(lista2):
        lista2.append("")
    for valores in range(len(columnas)):
        for columna1 in range(13):
            lista2[valores] += (lista[columna1][valores])
    for i in range(len(lista2)):
        print(lista2[i])
    return lista2

if __name__ ==  '__main__':
    crear_csv()
    listar_todos()

