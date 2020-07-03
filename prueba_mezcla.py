#luego cambio por unit test o algo mas prolijo.

import mezcla

def listar_archivos_prueba(nombre, cantidad, formato):
    l_ar_prueba = []
    for i in range(cantidad):
        l_ar_prueba.append(nombre + str(i) + formato)
    return l_ar_prueba


def main():
    l_entrada_prueba = listar_archivos_prueba("salidaPrueba", 10, ".csv")
    mezcla.mezclar_archivos(l_entrada_prueba, "salida_prueba_1.csv", 0)

main()
