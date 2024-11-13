import random

def archivoMatriz(nombre, a):

    nombreArchivo = "cost_" + nombre + ".txt"
    archivo = open(nombreArchivo, "w")
    
    for i in range(0,26):
        for j in range(0,26):
            if i == j:
                archivo.write("0 ")
            elif a == 1:
                archivo.write("1 ")
            else:
                archivo.write("2 ")
        archivo.write("\n")
    archivo.close()

    return

def archivoLinea(nombre):
    nombreArchivo = "cost_" + nombre + ".txt"
    archivo = open(nombreArchivo, "w")
    for i in range(0,26):
        archivo.write("1 ")
    return



archivoLinea("insert")
archivoMatriz("transpose", 1)
archivoMatriz("replace", 0)
archivoLinea("delete")
