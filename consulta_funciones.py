import reuti_codigo,str_hnd

#definicion de constantes

COMENTARIOS_FUNCION = 0
COMENTARIOS_CAMPO_AUTOR = 1
COMENTARIOS_CAMPO_AYUDA = 2
COMENTARIOS_GENERALES = 3
FUENTE_FUNCION = 0
FUENTE_PARAMETROS = 1
FUENTE_MODULO = 2
FUENTE_CODIGO = 3
NUMERAL = chr(35)

def listar_funciones():
    """
    [Autor: Claudio Gimenez]
    [Ayuda:
    Pre --> Abro el archivo fuente_unico.csv
    Post -->Armo cuadro de funciones encolumnado y devuelvo
    una lista de funciones]
    """
    archivo_codigo = open('fuente_unico.csv','r')
    funciones = reuti_codigo.armar_lista(archivo_codigo)
    numero=0
    
    while len(funciones)>numero:
        texto=''
        if numero < (len(funciones)-1):
            
            for i in range(0,2):
                columnas=reuti_codigo.generar_texto_encolumnado(50,funciones[numero])
                texto=texto+columnas[FUENTE_FUNCION]
                numero+=1
        
        else:
            columnas = reuti_codigo.generar_texto_encolumnado(50,funciones[numero])
            texto = columnas[FUENTE_FUNCION] + " " * 50 + "|"
            numero+=1
            
        print (texto)
        
        
    archivo_codigo.close()
    return(funciones)

def validar_opcion(opcion):
    """
    [Autor: Claudio Gimenez]
    [Ayuda:
    Pre --> Recibe la opcion que ingresa el usuario
    Post -->Retorna si la opciones valida, el nombre de la funcion y la opcion que luego
    voy a usar]
    """
    valido = False
    miopcion = ""
    nombre_funcion = ''
    if opcion[-1] == '?' or opcion[-1] == NUMERAL:
        valido = True
        miopcion = opcion[-1]
        nombre_funcion = opcion[:-1]
        
    elif opcion == 'imprimir ?todo':
        valido = True
        miopcion = 'imprimir ?todo'
            
    elif opcion[-5:] == '?todo' or opcion[-5:] == NUMERAL + 'todo':
        valido = True
        miopcion = opcion[-5:]
                
    return valido,nombre_funcion,miopcion

def validar_nombre_funcion(nombre_funcion,l_funciones):
    """
    [Autor: Claudio Gimenez]
    [Ayuda:
    Pre --> Recibe el nombre de la funcion y la lista de funciones
    Post -->Retorna si encontro la funcion y el nombre encontrado
    ]
    """
    posicion = 0
    encontrado = False
    nombre_encontrado=''
    while posicion < len(l_funciones) and not encontrado:
        if l_funciones[posicion] == nombre_funcion:
            encontrado = True
            nombre_encontrado=l_funciones[posicion]
        posicion+=1
    return encontrado,nombre_encontrado


def retornar_codigo(l_funcion,linea):
    """
    [Autor: Claudio Gimenez]
    [Ayuda:
    Pre --> Recibe la lista de funciones y la linea
    Post -->Retorna el codigo de la funcion
    ]
    """
    l_codigor = []
    for i in range(FUENTE_CODIGO,len(l_funcion[linea])):
            l_codigor.append(l_funcion[linea][i])
    return l_codigor

def retornar_comentario(l_comentarios,linea):
    """
    [Autor: Claudio Gimenez]
    [Ayuda:
    Pre --> Recibe la lista de funciones y la linea
    Post -->Retorna el comentario de la funcion
    ]
    """
    l_comentariosr = []
    for i in range(COMENTARIOS_GENERALES,len(l_comentarios[linea])):
            l_comentariosr.append(l_comentarios[linea][i])
    return l_comentariosr

def devolver_param_mod_autor_ayuda(l_funcion,l_comentraios,linea):
    """
    [Autor: Claudio Gimenez]
    [Ayuda:
    Pre --> Recibe la lista de funciones comentarios y la linea
    Post -->Retorna el parametros modulo autor y ayuda
    ]
    """
    t_param_mod_autor_ayuda = (l_funcion[linea][FUENTE_PARAMETROS],l_funcion[linea][FUENTE_MODULO],\
    l_comentraios[linea][COMENTARIOS_CAMPO_AUTOR],l_comentraios[linea][COMENTARIOS_CAMPO_AYUDA])
    
    parametros,modulo,autor,ayuda = t_param_mod_autor_ayuda
    
    ayuda = ayuda if ayuda else 'No hay ayuda para esta funcion'
            
    autor = autor if autor else 'No hay autores para esta funcion'
    
    return parametros,modulo,autor,ayuda

def mostrar_informacion(l_funcion,l_comentarios,nombre_encontrado,miopcion):
    """
    [Autor: Claudio Gimenez]
    [Ayuda:
    Pre --> Recibe la lista de funciones de comentarios nombre encontrado y miopcion
    Post -->Retorna parametro modulo autor ayuda lista de codigo y lista de comentarios
    ]
    """
    
    #abro archivos y los paso a listas
    
    
    contador_funciones = 0
    while contador_funciones < len(l_funcion) and nombre_encontrado \
    != l_funcion[contador_funciones][FUENTE_FUNCION] + "." + l_funcion[contador_funciones][FUENTE_MODULO]:
        contador_funciones+=1
    
    parametros,modulo,autor,ayuda = devolver_param_mod_autor_ayuda(l_funcion,l_comentarios,contador_funciones)
    l_codigo = []
    
    if miopcion == NUMERAL or miopcion == NUMERAL + 'todo':
        l_codigo = retornar_codigo(l_funcion,contador_funciones)

    
    contador_comentarios = 0
    while contador_comentarios < len(l_comentarios) and nombre_encontrado[:nombre_encontrado.find(".")] \
    != l_comentarios[contador_comentarios][COMENTARIOS_FUNCION]:
        contador_comentarios+=1
    
    l_comentario_linea = []
    
    if miopcion == NUMERAL or miopcion == NUMERAL + 'todo':
        l_comentario_linea = retornar_comentario(l_comentarios,contador_comentarios)
         

        
    return parametros,modulo,autor,ayuda,l_codigo,l_comentario_linea   
    
def imprimir_funcion_opcion_pregunta(parametros,modulo,autor,ayuda):
    """
    [Autor: Claudio Gimenez]
    [Ayuda:
    Pre --> Recibe parametros modulo autor ayuda
    Post -->imprime los datos de la opcion funcion pregunta
    ]
    """
            
    print(f"Parmetros: {parametros}\nModulo: {modulo}\n{autor}\n{ayuda}")
    
def imp_desc_todas_func(l_funcion,l_comentarios,miopcion):
    """
    [Autor: Claudio Gimenez]
    [Ayuda:
    Pre --> Recibe la lista de funciones de comentarios y miopcion
    Post --> imprime la ayuda de todas las fuciones o todo de las funciones
    ]
    """
    #aca imprimo la descripcion de todas las funciones
        
    for i in range(0,len(l_funcion)):
                
        parametros,modulo,autor,ayuda = devolver_param_mod_autor_ayuda(l_funcion,l_comentarios,i)
        
        print('Datos de la funcion:',l_funcion[i][FUENTE_FUNCION] + '.' + l_funcion[i][FUENTE_MODULO] ,'\n')
        imprimir_funcion_opcion_pregunta(parametros,modulo,autor,ayuda)
        print('\n')
        if miopcion == NUMERAL + 'todo':
            
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
    """
    [Autor: Claudio Gimenez]
    [Ayuda:
    Pre --> Recibe la lista de funciones y de comentarios
    Post -->Genera el archivo txt de ayuda para las funciones
    ]
    """
    archivo = open("ayuda_funciones.txt", 'w')

    archivo.seek(0, 1)
    texto=''
    for i in range(0,len(l_funcion)):
        
        texto = 'Ayuda de la funcion: ' + l_funcion[i][FUENTE_FUNCION] + '.' + l_funcion[i][FUENTE_MODULO]
        parametros,modulo,autor,ayuda = devolver_param_mod_autor_ayuda(l_funcion,l_comentarios,i)

        texto = texto + ' Parametros: ' + parametros + ' Modulo: ' + modulo + ' ' + autor + ' ' + ayuda
        
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
    """
    [Autor: Claudio Gimenez]
    [Ayuda:
    Pre --> Recibe la lista de funciones con que genero la tabla pide se ingrese la consulta
    Post -->Llama a otras funciones muestra la informacion necesaria
    ]
    """
    opcion = input("Función: ")
    while opcion!='':
        opcion_elegida,nombre_funcion,miopcion=validar_opcion(opcion)
        if opcion_elegida: #si la opcion elegida es valida
            
            #abro archivos y los paso a listas
            archivo_codigo = open('fuente_unico.csv','r')
            archivo_comentarios = open('comentarios.csv','r')
            l_funcion = []
            l_comentarios = []
    
            for linea in archivo_codigo:
                funcion = linea.rstrip("\n").split(",")
                str_hnd.desprocesar_comas(funcion)
                l_funcion.append(funcion)
            for linea in archivo_comentarios:
                comentarios = linea.rstrip("\n").split(",")
                str_hnd.desprocesar_comas(comentarios)
                l_comentarios.append(comentarios)
            
            if miopcion == '?todo' or miopcion == NUMERAL + 'todo' or miopcion == 'imprimir ?todo':
                #aca muestro todo de todas las funciones segun la opcion # o ? o imprimirtodo
                
                                
                if miopcion == '?todo' or miopcion == NUMERAL + 'todo':
                    imp_desc_todas_func(l_funcion,l_comentarios,miopcion)
                
                if miopcion == 'imprimir ?todo':
                    print ('Se genero el archivo ayuda_funciones.txt')
                    generar_txt(l_funcion,l_comentarios)
            else:    
                encontrado, nombre_encontrado = validar_nombre_funcion(nombre_funcion, funciones)
                if encontrado:
                    #print("Aca muestro las cosas de una funcion")
                    
                    parametros,modulo,autor,ayuda,l_codigo,l_comentario_linea = mostrar_informacion(l_funcion,l_comentarios,nombre_encontrado,miopcion)                    
                    if miopcion == '?':
                        print("Datos de funcion:",nombre_encontrado,"\n")
                        imprimir_funcion_opcion_pregunta(parametros,modulo,autor,ayuda)
                        
                        
                    if miopcion == NUMERAL:
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
    