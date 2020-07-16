import ordenamiento
import mezcla
import os
import reuti_codigo

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
    lista_cod.append(codigo); lista_com.append(comentarios)
    limpiar_archivos(lista_cod, lista_com)

def ejecutar(opcion):

    if opcion == '1':
        pass
    elif opcion == '2':
        pass
    elif opcion == '3':
        reuti_codigo.generar_analizador()
    elif opcion == '4':
        pass
    elif opcion == '5':
        pass
    elif opcion == 'todavia no se ingreso nada como opcion':
        print("Bienvenido al programa!!!!!")
    else:
        print("No se eligio una opcion correcta")

def menu(display):

    opcion = 'todavia no se ingreso nada como opcion'
    while opcion != '6':
        ejecutar(opcion)
        print(display)
        opcion = input(">>> ")
    

def principal():

    generar_fuente_y_com()
    display = "1-Panel general de funciones.\n"
    display += "2-Consulta de funciones.\n"
    display += "3-Analizador de reutilizacion de codigo.\n"
    display += "4-Arbol de invocacion.\n"
    display += "5-Informacion por desarrolador.\n"
    display += "6-Cerrar programa."
    menu(display)

if __name__ == '__main__':
    principal()

