import estructura


def funcion_principal_estructuracion_codigo():
    """
    [Autor: Francisco Pereira]
    [Ayuda: Funcion principal del programa]
    """
    estructura.generar_fuente_y_com()
    display = "1-Panel general de funciones.\n"
    display += "2-Consulta de funciones.\n"
    display += "3-Analizador de reutilizacion de codigo.\n"
    display += "4-Arbol de invocacion.\n"
    display += "5-Informacion por desarrolador.\n"
    display += "6-Cerrar programa."
    estructura.menu(display)

if __name__ == '__main__':
    funcion_principal_estructuracion_codigo()

