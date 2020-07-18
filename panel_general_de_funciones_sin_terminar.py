import reuti_codigo
from reuti_codigo import leer_linea_archivo
#Falta agregar contadores de todo(buscando como editar la funcion armar_lista) y crear nuevo archivo csv para guardar

def armar_lista_parametros(archivo_codigo):
    
    lista_funciones = []
    linea = leer_linea_archivo(archivo_codigo) 
                                                      
    while linea != ['']:
        funcion = f'{linea[1]}'
     #   x=funcion.count('/')       con esto queria contar cantidad de parametros
                                    
     #   lista_funciones.append(x)  pero tengo que crear o editar el armar_lista
        lista_funciones += [funcion]
        linea = leer_linea_archivo(archivo_codigo)

    archivo_codigo.seek(0)

    return lista_funciones
def lineas_codigo(archivo_codigo):

    lista_lineas = []
    linea = leer_linea_archivo(archivo_codigo) 
                                                      
    while linea != ['']:
        funcion = f'{linea[3]}'
                                       
        lista_funciones += [funcion]
        linea = leer_linea_archivo(archivo_codigo)

    archivo_codigo.seek(0)

    return lista_funciones



def listar_todo():
    numero = 0
    archivo_codigo = open('salida_codigo.csv','r')
    funciones = reuti_codigo.armar_lista(archivo_codigo)
    parametros= armar_lista_parametros(archivo_codigo)
    while len(funciones)>numero :
        texto=''
        texto2=''
        columnas=reuti_codigo.generar_texto_encolumnado(40,funciones[numero])
        columnas2=reuti_codigo.generar_texto_encolumnado(80, parametros[numero])
       
        texto=texto+columnas[0]
        texto2=texto2+columnas2[0]
      
        print(texto,texto2)
        numero2= 0
        numero += 1
    
    print (numero,"funciones")
    
        
        
    archivo_codigo.close()
    
    
    return (parametros)
      
        


parametros=listar_todo()

