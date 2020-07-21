"""
Para pruebas del punto 3
Este modulo toma el texto despues de un def
hasta un return u otro def
"""
import archivos_programa as a_p
def guardar_funcion(archivo):
    """
    Pre: Ingresa el archivo con una funcion ya 
    encontrada
    Post: Devuelve todo el texto separado por comas linea a linea
    """
    codigo = ""
    linea = archivo.readline()
    while ('return ' not in linea) and ('def ' not in linea) and linea:
        linea = linea[:linea.find('\n')]
        codigo += linea + ','
        linea = archivo.readline()
    
    if 'return ' in linea:
        linea = linea[:linea.find('\n')]
        codigo += linea + ','
    
    return codigo, linea
