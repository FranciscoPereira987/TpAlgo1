import reuti_codigo
from reuti_codigo import leer_linea_archivo
import csv
#voy a cambiar el metodo de impresion del archivo hoy despues de clase
#falta buscar cantidad de returns, si tiene comentarios
#falta agregar autor, ayuda
#falta ordenar la impresion
#falta ver si tiene comentarios cada funcion
#necesito ayuda con como ver si tiene ayuda y comentarios
def armar_lista_parametros(archivo_codigo):
    """
    [Autor: Nicolas Valenzuela]
    [Ayuda: Recibe el archivo csv, arma una lista con la cantidad de parametros
    devuelve la lista armada con la cantidad de parametros por funcion]
    """
    lista_funciones = []
    linea = reuti_codigo.leer_linea_archivo(archivo_codigo) 
                                                      
    while linea != ['']:
        funcion = f'{linea[1]}'
        x=funcion.count('/')    

        if x > 0 :
            lista_funciones.append(x+1)
        elif len(funcion) > 2 :
                lista_funciones.append(1)
        else:
                lista_funciones.append(x)

        linea = leer_linea_archivo(archivo_codigo)

    archivo_codigo.seek(0)

    return lista_funciones
def cantidad_de_lineas():
    """
    [Autor: Nicolas Valenzuela]
    [Ayuda: Arma una lista con la cantidad de lineas
    devuelve la lista armada con la cantidad de lineas por funcion]
    """
    archivo_codigo = open('salida_codigo.csv','r')
    palabra = ','   
    ocurrencias = []
    for lineas in archivo_codigo:
            if palabra in lineas :
                x = lineas.count(palabra)                
                ocurrencias.append(x+1)
            else:
                ocurrencias.append(0)
    archivo_codigo.close()            
    return ocurrencias
def lineas_codigo(archivo_codigo):

    lista_lineas = []
    linea = leer_linea_archivo(archivo_codigo) 
                                                      
    while linea != ['']:
        funcion = f'{linea[3]}'
                                       
        lista_funciones += [funcion]
        linea = leer_linea_archivo(archivo_codigo)

    archivo_codigo.seek(0)

    return lista_funciones

def cantidad_de_if(archivo_codigo):
    palabra = ' if '
    palabra2 = ' elif '
    ocurrencias = []
  
    for row in archivo_codigo:
            if palabra in row or palabra2 in row:
                x = row.count(palabra)
                x = x + row.count(palabra2)
                ocurrencias.append(x)
            else:
                ocurrencias.append(0)
    return ocurrencias
def cantidad_de_for():
    archivo_codigo = open('salida_codigo.csv','r')
    palabra = ' for '   
    ocurrencias = []
    for lineas in archivo_codigo:
            if palabra in lineas :
                x = lineas.count(palabra)                
                ocurrencias.append(x)
            else:
                ocurrencias.append(0)
    archivo_codigo.close()            
    return ocurrencias
def cantidad_de_while():
    archivo_codigo = open('salida_codigo.csv','r')
    palabra = ' for '   
    ocurrencias = []
    for lineas in archivo_codigo:
            if palabra in lineas :
                x = lineas.count(palabra)                
                ocurrencias.append(x)
            else:
                ocurrencias.append(0)
    archivo_codigo.close()            
    return ocurrencias
def cantidad_de_break():
    archivo_codigo = open('salida_codigo.csv','r')
    palabra = ' break '   
    ocurrencias = []
    for lineas in archivo_codigo:
            if palabra in lineas :
                x = lineas.count(palabra)                
                ocurrencias.append(x)
            else:
                ocurrencias.append(0)
    archivo_codigo.close()            
    return ocurrencias

def cantidad_de_exit():
    archivo_codigo = open('salida_codigo.csv','r')
    palabra = ' exit '   
    ocurrencias = []
    for lineas in archivo_codigo:
            if palabra in lineas :
                x = lineas.count(palabra)                
                ocurrencias.append(x)
            else:
                ocurrencias.append(0)
    archivo_codigo.close()            
    return ocurrencias
def lista_ayuda():
    archivo_codigo = open('salida_comentarios.csv','r')
    lista_ayuda = []
    for i in archivo_codigo:
        a=i.count('yuda')
        b=i.count('AYUDA')
        if a != 0 or b != 0:
            lista_ayuda.append('Si')
        else:
            lista_ayuda.append('No')
    archivo_codigo.seek(0)
    archivo_codigo.close
    return lista_ayuda
def funcion_autor():
    archivo_codigo = open('salida_comentarios.csv','r')
    lista_autores = []
    linea = leer_linea_archivo(archivo_codigo) 
                                                      
    while linea != ['']:
        funcion = f'{linea[1]}'                                    
        lista_autores += [funcion]
        linea = leer_linea_archivo(archivo_codigo)

    archivo_codigo.seek(0)
    
    return lista_autores


def listar_todo():
    numero = 0
    archivo_codigo = open('salida_codigo.csv','r')
    archivo_codigo2=open('salida_comentarios.csv','r')
    funciones = reuti_codigo.armar_lista(archivo_codigo)
    parametros= armar_lista_parametros(archivo_codigo)
    cant_lineas= cantidad_de_lineas()
    cant_if=cantidad_de_if(archivo_codigo)
    cant_for=cantidad_de_for()
    cant_while=cantidad_de_while()
    cant_break=cantidad_de_break()
    cant_exit=cantidad_de_exit()
    autores=funcion_autor()
   # ayuda=lista_ayuda()
    print (autores)
    while len(funciones)>numero :
        texto=''
        texto2=''
        texto3=''
        texto4=''
        texto5=''
        texto6=''
        texto7=''
        texto8=''
        columnas=reuti_codigo.generar_texto_encolumnado(40,funciones[numero])
        columnas2=reuti_codigo.generar_texto_encolumnado(2, str(parametros[numero]))
        columnas3=reuti_codigo.generar_texto_encolumnado(2,str(cant_if[numero]))
        columnas4=reuti_codigo.generar_texto_encolumnado(2,str(cant_for[numero]))
        columnas5=reuti_codigo.generar_texto_encolumnado(2,str(cant_while[numero]))
        columnas6=reuti_codigo.generar_texto_encolumnado(2,str(cant_lineas[numero]))
    #    columnas7=reuti_codigo.generar_texto_encolumnado(20,ayuda[numero])
     #   columnas8=reuti_codigo.generar_texto_encolumnado(20,autores[numero])
        texto=texto+columnas[0]
        texto2=texto2+columnas2[0]
        texto3=texto3+columnas3[0]
        texto4=texto4+columnas4[0]
        texto5=texto5+columnas5[0]
        texto6=texto6+columnas6[0]
     #   texto7=texto7+columnas7[0]
     #   texto8=texto8+columnas8[0]
        print(texto,texto2,texto3,texto4,texto5,texto6)#,texto8)#,texto7)
        numero2= 0
        numero += 1

  #  print (numero,"funciones")
    
        
        
    archivo_codigo.close()
    archivo_codigo2.close()
    
    
    return (funciones,parametros,cant_if,cant_for,cant_while,cant_break,cant_exit,cant_lineas,autores)#,ayuda)





def crear_csv(funciones,parametr,cant_if,cant_for,cant_while,cant_break,cant_exit,cant_lineas,autores,ayuda):
    
   
    with open('panel_general.csv', 'w', newline='') as miarchivo:
        parametros = ['FUNCION','Parámetros','Líneas','Invocaciones','Returns','if/elif','for','while','break','Exit','Coment','Ayuda','Autor']
        escribir = csv.DictWriter(miarchivo, fieldnames=parametros)
        escribir.writeheader()
        for i in range(len(funciones) ):
            
            escribir.writerow({'FUNCION': funciones[i], 'Parámetros' : parametr[i], 'Líneas' : cant_lineas[i], 'if/elif' : cant_if[i],
                               'for' : cant_for[i], 'while' : cant_while[i], 'break' : cant_break[i], 'Exit' : cant_exit[i],
                               'Ayuda' : ayuda[i], 'Autor' : autores[i]})

        return ()
        
        

        


funciones, parametros,cant_if,cant_for,cant_while,cant_break,cant_exit,cant_lineas, autores=listar_todo()
ayuda=lista_ayuda()
crear_csv(funciones,parametros,cant_if,cant_for,cant_while,cant_break,cant_exit,cant_lineas,autores,ayuda)

