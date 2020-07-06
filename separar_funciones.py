def leer_archivo(archivo):
    #leo una linea del archivo que me pasan por parametro
    linea=archivo.readline()
    #si hay linea saco el espacio al final y guardo en variable
    #para devolver la linea sino devuelvo un vacio
    if linea:
        devolver=linea.strip('\n')
    else:devolver=''
    return devolver
        

def listar_archivo():
    #declaro contador en 0
    contador=0
    '''abro archivo y paso el contenido a la variable, luego leo la primera
    linea pasando como parametro la variable ar_programa como parametro de
    la funcion y guardo la primera linea en ar_codigo''' 
    ar_programa=open("modular.py",'r')
    ar_codigo=leer_archivo(ar_programa)
    '''mientras la linea no tenga un vacio y contador<=1, pregunto si
    en linea hay un def o return y en ese caso sumo 1 al contador, si
    contador es mayor a cero y menor igual a dos imprimo la linea, luego
    cuando evalua contador en 2 sale del ciclo y ciero el archivo.'''
    l_codigo=[]
    while ar_codigo!='':
        if 'def' in ar_codigo:
            while 'return' not in ar_codigo:
                if chr(39)+chr(39)+chr(39) in ar_codigo:
                    ar_codigo=leer_archivo(ar_programa)
                    while chr(39)+chr(39)+chr(39) not in ar_codigo and ar_codigo!='':
                        ar_codigo=leer_archivo(ar_programa)
                    ar_codigo=leer_archivo(ar_programa)    
                #print(ar_codigo, end="\n")    
                l_codigo.append(ar_codigo)
                ar_codigo=leer_archivo(ar_programa)
            #print(ar_codigo, end="\n")
            l_codigo.append(ar_codigo)    
            ar_codigo=leer_archivo(ar_programa)
        else:
            ar_codigo=leer_archivo(ar_programa)
    ar_programa.close()
    return l_codigo

print (listar_archivo())
'''lista=listar_archivo()
for i in lista:
    print(i)'''