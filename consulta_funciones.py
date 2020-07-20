import reuti_codigo

def listar_funciones():
    """
    [Autor: Claudio Gimenez]
    [Ayuda:
    Pre --> Abro el archivo fuente_unico.csv
    Post -->Armo cuadro de funciones encolumnado y devuelvo
    una lista de funciones]
    """
    archivo_codigo = open('salida_codigo.csv','r')
    funciones = reuti_codigo.armar_lista(archivo_codigo)
    numero=0
    
    while len(funciones)>numero:
        texto=''
        for i in range(0,2):
            columnas=reuti_codigo.generar_texto_encolumnado(40,funciones[numero])
            texto=texto+columnas[0]
            numero+=1
        print (texto)
        
        
    archivo_codigo.close()
    return(funciones)

def validar_opcion(opcion):
    valido = False
    miopcion = ""
    nombre_funcion = ''
    if opcion[-1] == '?' or opcion[-1] == '#':
        valido = True
        miopcion = opcion[-1]
        nombre_funcion = opcion[:-1]
        
    elif opcion[0:8] ==  'imprimir':
        valido = True
        miopcion = 'imprimir ?todo'
        #miopcion = opcion[-14:]
        #nombre_funcion = opcion[:-14]
    
    elif opcion[-5:] == '?todo' or opcion[-5:] == '#todo':
        valido = True
        miopcion = opcion[-5:]
        #nombre_funcion = opcion[:-5]
        
        
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

#l_funcion[contador_funciones][1]
def retornar_param(l_funcion,linea,posicion):
    #retorno parametro o modulo de funcion
    #parametros = ''
    parametros = l_funcion[linea][posicion]
    return parametros

def retornar_mod(l_funcion,linea,posicion):
    modulo = l_funcion[linea][posicion]
    return modulo

def retornar_autor(l_funcion,linea,posicion):
    autor = l_funcion[linea][posicion]
    return autor

def retornar_ayuda(l_funcion,linea,posicion):
    ayuda = l_funcion[linea][posicion]
    return ayuda

def retornar_codigo(l_funcion,linea):
    l_codigor = []
    for i in range(3,len(l_funcion[linea])):
            l_codigor.append(l_funcion[linea][i])
    return l_codigor

def retornar_comentario(l_comentarios,linea):
    l_comentariosr = []
    for i in range(3,len(l_comentarios[linea])):
            l_comentariosr.append(l_comentarios[linea][i])
    return l_comentariosr

def mostrar_informacion(l_funcion,l_comentarios,nombre_encontrado,miopcion):
    #abro archivos y los paso a listas
    '''
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
    '''
    #if miopcion == '?':
    parametros = ''
    modulo = ''
    contador_funciones = 0
    while contador_funciones < len(l_funcion) and nombre_encontrado \
    != l_funcion[contador_funciones][0] + "." + l_funcion[contador_funciones][2]:
        contador_funciones+=1
    parametros = retornar_param(l_funcion,contador_funciones,1) #l_funcion[contador_funciones][1]
    modulo = retornar_mod(l_funcion,contador_funciones,2) #l_funcion[contador_funciones][2]
    l_codigo = []
    
    if miopcion == '#' or miopcion == '#todo':
        l_codigo = retornar_codigo(l_funcion,contador_funciones)
#         
#         for i in range(3,len(l_funcion[contador_funciones])):
#             l_codigo.append(l_funcion[contador_funciones][i])
    
    autor = ''
    ayuda = ''
    contador_comentarios = 0
    while contador_comentarios < len(l_comentarios) and nombre_encontrado[:nombre_encontrado.find(".")] \
    != l_comentarios[contador_comentarios][0]:
        contador_comentarios+=1
    autor = retornar_autor(l_comentarios,contador_comentarios,1) #l_comentarios[contador_comentarios][1]
    ayuda = retornar_ayuda(l_comentarios,contador_comentarios,2) #l_comentarios[contador_comentarios][2]
    l_comentario_linea = []
    
    if miopcion == '#' or miopcion == '#todo':
        l_comentario_linea = retornar_comentario(l_comentarios,contador_comentarios)
#         
#         for i in range(3,len(l_comentarios[contador_comentarios])):
#             l_comentario_linea.append(l_comentarios[contador_comentarios][i])
            
    #print(l_funcion)
    #print(l_comentarios)
    #print(l_comentario_linea)
    return parametros,modulo,autor,ayuda,l_codigo,l_comentario_linea
    #print(ayuda,'parametros: ',parametros,'modulo: ',modulo,autor)
    
    #archivo_codigo.close()
    #return l_funcion, l_comentarios    
    
def imprimir_funcion_opcion_pregunta(parametros,modulo,autor,ayuda):
    #print(ayuda,'parametros: ',parametros,'modulo: ',modulo,autor)
    if ayuda:
        print(ayuda)
    else:
        print('No hay ayuda para esta funcion')
    if autor:
        print(autor)
    else:
        print('No hay autor para esta funcion')
    print('Parametros:',parametros)
    print('Modulo:',modulo)
    
def imp_desc_todas_func(l_funcion,l_comentarios,miopcion):
    #aca imprimo la descripcion de todas las funciones
    #print('aca imprimo la descripcion de todas las funciones')
    
    for i in range(0,len(l_funcion)):
        parametros,modulo = l_funcion[i][1],l_funcion[i][2]
        ayuda,autor = l_comentarios[i][1],l_comentarios[i][2]
        #print(parametros,modulo,ayuda,autor)
        print('Datos de la funcion:',l_funcion[i][0],'\n')
        imprimir_funcion_opcion_pregunta(parametros,modulo,autor,ayuda)
        print('\n')
        if miopcion == '#todo':
            #l_codigo = ''
            #l_comentario_linea = ''
            print("Este es el codigo de la funcion:",'\n')
            l_codigo = retornar_codigo(l_funcion,i)
            l_comentario_linea = retornar_comentario(l_comentarios,i)
            
            for i in l_codigo:
                print(i)
            print('\n')
            if len(l_comentario_linea) == 0:
                print('La funcion no tiene comentarios adicionales','\n')
            else:    
                print("Estos son los comentarios generales de la funcion:",'\n')
                for i in l_comentario_linea:
                    print(i)
                print('\n')   
    
def generar_txt(l_funcion,l_comentarios):
    archivo = open(" ayuda_funciones.txt", 'w')

    archivo.seek(0, 1)
    texto=''
    for i in range(0,len(l_funcion)):
        parametros,modulo = l_funcion[i][1],l_funcion[i][2]
        ayuda,autor = l_comentarios[i][1],l_comentarios[i][2]
        texto = 'Ayuda de la funcion: ' + l_funcion[i][0] + '.' + l_funcion[i][2]
        if ayuda:
            texto = texto+' '+ayuda
        else:
            texto = texto + ' ' + 'No hay ayuda para esta funcion'
        if autor:
            texto = texto+' '+autor
        else:
            texto = texto + ' ' + 'No hay autor para esta funcion'
        texto = texto + ' ' + 'modulo: '+ modulo
        texto = texto + ' ' + 'parametros: '+ parametros #+ '\n'
        contador = 0
        for i in range(0,len(texto)):
            archivo.write(texto[i])
            contador+=1
            if contador == 80:
                archivo.write('\n')
                contador = 0
        archivo.write('\n')
        archivo.write('\n')
        
    archivo.close

def ingresar_opcion(funciones):
    opcion = input("Función: ")
    #encontrado,nombre_funcion = validar_nombre_funcion(nombre,funciones)
    #opcion = nombre[nombre.find(nombre_funcion)+len(nombre_funcion):]
    while opcion!='':
        opcion_elegida,nombre_funcion,miopcion=validar_opcion(opcion)
        #encontrado,nombre_encontrado = validar_nombre_funcion(nombre_funcion,funciones)
        
        if opcion_elegida: #si la opcion elegida es valida
            
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
            
            if miopcion == '?todo' or miopcion == '#todo' or miopcion == 'imprimir ?todo':
                #aca muestro todo de todas las funciones segun la opcion # o ? o imprimirtodo
                #print('aca muestro o todo o genero ayuda_funciones.txt')
                #mostrar_todo(miopcion)
                
                if miopcion == '?todo' or miopcion == '#todo':
                    imp_desc_todas_func(l_funcion,l_comentarios,miopcion)
                
                if miopcion == 'imprimir ?todo':
                    print ('Se genero el archivo ayuda_funciones.txt')
                    generar_txt(l_funcion,l_comentarios)
#                 for funcion in l_funcion:
#                     parametros,modulo,autor,ayuda,l_codigo,l_comentario_linea = mostrar_informacion(l_funcion,l_comentarios,funcion[0] + '.' + funcion[2],miopcion)
#                     if miopcion == '?todo':
#                         print('Datos de la funcion:',funcion[0],'\n')
#                         imprimir_funcion_opcion_pregunta(parametros,modulo,autor,ayuda)
#                         print('\n')
#                     if miopcion == '#todo':
#                         print('Datos de la funcion:',funcion[0],'\n')
#                         imprimir_funcion_opcion_pregunta(parametros,modulo,autor,ayuda)
#                         print('\n')
#                         print("Este es el codigo de la funcion:",'\n')
#                         for i in l_codigo:
#                             print(i)
#                         print('\n')    
#                         print("Estos son los comentarios generales de la funcion:",'\n')
#                         for i in l_comentario_linea:
#                             print(i)
#                         print('\n')        
            else:    
                encontrado, nombre_encontrado = validar_nombre_funcion(nombre_funcion, funciones)
                if encontrado:
                    #print("Aca muestro las cosas de una funcion")
                    parametros,modulo,autor,ayuda,l_codigo,l_comentario_linea = mostrar_informacion(l_funcion,l_comentarios,nombre_encontrado,miopcion)
                    if miopcion == '?':
                        print("Datos de funcion:",nombre_encontrado,"\n")
                        imprimir_funcion_opcion_pregunta(parametros,modulo,autor,ayuda)
                        
                    if miopcion == '#':
                        print("Datos de la Funcion:",nombre_encontrado,"\n")
                        imprimir_funcion_opcion_pregunta(parametros,modulo,autor,ayuda)
                        print("Este es el codigo de la funcion:")
                        for i in l_codigo:
                            print(i)
                        print("Estos son los comentarios generales de la funcion:")
                        for i in l_comentario_linea:
                            print(i)
                else:
                    print("La funcion es incorrecta escriba nombre de funcion.modulo como esta en el cuadro seguido la opcion ? #")
            archivo_codigo.close()
            archivo_comentarios.close()
        else:
            print("Opcion invalida las opciones son ? # para consultar una funcion o ?todo #todo imprimir ?todo para todas las funciones")
        
        opcion = input("Funcion: ")
    return opcion
    #print(opcion)

#print(listar_funciones())
funciones = listar_funciones()
ingresar_opcion(funciones)
    

