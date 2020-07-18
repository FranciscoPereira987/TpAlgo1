import reuti_codigo

def listar_funciones():
    
    archivo_codigo = open('salida_codigo.csv','r')
    funciones = reuti_codigo.armar_lista(archivo_codigo)
    numero=0
    
    while len(funciones)>numero:
        #for i in range(0,2):
            #print(funciones[numero] ,sep="\t", end="|")
        #columnas=reuti_codigo.generar_texto_encolumnado(40,funciones[numero])
        #texto=columnas[0]
        texto=''
        for i in range(0,2):
            columnas=reuti_codigo.generar_texto_encolumnado(40,funciones[numero])
            texto=texto+columnas[0]
            numero+=1
        print (texto)
        
        #funciones = reuti_codigo.armar_diccionario(funciones)
    archivo_codigo.close()
    return(funciones)
    #return lista_funciones

def validar_opcion(opcion):
    valido = False
    miopcion = ""
    nombre_funcion = ''
    if opcion[-1] == '?' or opcion[-1] == '#':
        valido = True
        miopcion = opcion[-1]
        nombre_funcion = opcion[:-1]
        
    elif opcion[-5:] == '?todo' or opcion[-5:] == '#todo':
        valido = True
        miopcion = opcion[-5:]
        #nombre_funcion = opcion[:-5]
        
    elif opcion[-14:] ==  'imprimir ?todo':
        valido = True
        miopcion = opcion[-14:]
        #nombre_funcion = opcion[:-14]
        
    return valido,nombre_funcion,miopcion

def validar_nombre_funcion(nombre_funcion,l_funciones):
    posicion = 0
    encontrado = False
    nombre_encontrado=''
    while posicion < len(l_funciones) and not encontrado:
        if l_funciones[posicion] == nombre_funcion:
            encontrado = True
            nombre_encontrado=l_funciones[posicion]
        posicion+=1
    return encontrado,nombre_encontrado

def leer(archivo):
    '''
    Funcion que lee una linea del archivo y devuelve los valores leidos
    cod_sucursal, cod_articulo, cant_vendida, imp_total.    En caso de llegar
    a fin de archivo devolverá 4 valores vacios    separados por comas.
    '''
    linea = archivo.readline()
    if linea:
        devolver = linea.rstrip("\n").split(",")
    else:
        devolver = "","","0","0"
    return devolver


def mostrar_informacion(miopcion,nombre_encontrado):
    #abro archivos y los paso a listas
    archivo_codigo = open('salida_codigo.csv','r')
    archivo_comentarios = open('salida_comentarios.csv','r')
    l_funcion = []
    l_comentarios = []
    
    for linea in archivo_codigo:
        funcion = linea.rstrip("\n").split(",")
        l_funcion.append(funcion)
    for linea in archivo_comentarios:
        comentarios = linea.rstrip("\n").split(",")
        l_comentarios.append(comentarios)
    
    if miopcion == '?':
        parametros = ''
        modulo = ''
        contador = 0
        while contador < len(l_funcion) and nombre_encontrado \
        != l_funcion[contador][0] + "." + l_funcion[contador][2]:
            contador+=1
        parametros = l_funcion[contador][1]
        modulo = l_funcion[contador][2]
        
    print(l_funcion)
    print(l_comentarios)
    archivo_codigo.close()
    return l_funcion, l_comentarios    
    
    

def ingresar_opcion(funciones):
    opcion = input("Función: ")
    #encontrado,nombre_funcion = validar_nombre_funcion(nombre,funciones)
    #opcion = nombre[nombre.find(nombre_funcion)+len(nombre_funcion):]
    while opcion!='':
        opcion_elegida,nombre_funcion,miopcion=validar_opcion(opcion)
        #encontrado,nombre_encontrado = validar_nombre_funcion(nombre_funcion,funciones)
        
        if opcion_elegida:
            if miopcion == '?todo' or miopcion == '#todo' or miopcion == 'imprimir ?todo':
                #aca muestro todo de todas las funciones segun la opcion # o ? o imprimirtodo
                print('aca muestro o todo o genero ayuda_funciones.txt')
                #mostrar_todo(miopcion)
            else:    
                encontrado, nombre_encontrado = validar_nombre_funcion(nombre_funcion, funciones)
                if encontrado:
                    print("Aca muestro las cosas de una funcion")
                    mostrar_informacion(miopcion,nombre_encontrado)
                else:
                    print("La funcion es incorrecta")
        else:
            print("opcion invalida")
        
        opcion = input("Funcion: ")
    return opcion
    #print(opcion)

#print(listar_funciones())
funciones = listar_funciones()
ingresar_opcion(funciones)
    

