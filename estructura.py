import ordenamiento, mezcla, os, reuti_codigo
import consulta_funciones, arbol_invo, info_participacion
import panel_general_de_funciones

def limpiar_archivos(lista_codigos, lista_comentarios):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Elimina archivos luego de que hayan sido mergeados]
    """
    lista = lista_codigos + lista_comentarios
    for archivo in lista:
        os.remove(archivo)

def listar_archivos(archivo_con_rutas):
    """
    [Autor: Francisco Pereira]
    [Ayuda: Lee un archivo que contiene rutas
    y coloca las mismas en una lista]
    """
    lista_rutas = []
    archivo = open(archivo_con_rutas, 'r')
    linea = archivo.readline()

    while linea:
        lista_rutas.append(linea.rstrip('\n'))
        linea = archivo.readline()

    archivo.close() 

    return lista_rutas

def generar_fuente_y_com():
    """
    [Autor: Francisco Pereira]
    [Ayuda: Genera los archivos fuente_unico y comentarios
    con el formato pedido]
    """
    comentarios, codigo = ordenamiento.main_ordenamiento()
    lista_cod = listar_archivos(codigo)
    lista_com = listar_archivos(comentarios)
    mezcla.mezclar_archivos(lista_cod, 'fuente_unico.csv', 0)
    mezcla.mezclar_archivos(lista_com, 'comentarios.csv', 0)
    lista_cod.append(codigo)
    lista_com.append(comentarios)
    limpiar_archivos(lista_cod, lista_com)


def esperar():
    """
    [Autor: Francisco Pereira]3
    [Ayuda: espera a que el usuario ingrese
    algo para que se continue con la ejecutcion del programa]
    """
    print("\n\n")
    print("Ingrese cualquier comando para regresar al menu")
    input(">>>")

def ejecutar(opcion):
    """
    [Autor: Francisco Pereira]
    [Ayuda: direcciona la opcion elegida para que
    el usuario obtenga la salida esperada
    ]
    """
    if opcion == '1':
        panel_general_de_funciones.crear_csv()
        panel_general_de_funciones.listar_todos()
        esperar()

    elif opcion == '2':
        funciones = consulta_funciones.listar_funciones()
        consulta_funciones.ingresar_opcion(funciones)

    elif opcion == '3':
        reuti_codigo.generar_analizador()
         
    elif opcion == '4':
        arbol_invo.arbol_invocacion()
        esperar()
        
    elif opcion == '5':
        info_participacion.informar_participacion()
        esperar()
    
    elif opcion == 'todavia no se ingreso nada como opcion':
        print("Bienvenido al programa!!!!!")

    else:
        print("No se eligio una opcion correcta")

def menu(display):
    """
    [Autor: Francisco Pereira]
    [Ayuda: menu del programa]
    """
    opcion = 'todavia no se ingreso nada como opcion'
    while opcion != '6':
        ejecutar(opcion)
        print("\n\n")
        print(display)
        opcion = input(">>> ")
    
