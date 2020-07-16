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
        nombre_funcion = opcion[:-5]
        
    elif opcion[-14:] ==  'imprimir ?todo':
        valido = True
        miopcion = opcion[-14:]
        nombre_funcion = opcion[:-14]
        
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
        
def ingresar_opcion(funciones):
    opcion = input("Función: ")
    #encontrado,nombre_funcion = validar_nombre_funcion(nombre,funciones)
    #opcion = nombre[nombre.find(nombre_funcion)+len(nombre_funcion):]
    while opcion!='':
        opcion_elegida,nombre_funcion,miopcion=validar_opcion(opcion)
        encontrado,nombre_encontrado = validar_nombre_funcion(nombre_funcion,funciones)
        
        if opcion_elegida:
            encontrado, nombre_encontrado = validar_nombre_funcion(nombre_funcion, funciones)
            if encontrado:
                print("Aca muestro las cosas")
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
    

