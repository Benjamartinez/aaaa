import os 
import csv

def menu():
    print("1.- Ingresar Alumno")
    print("1.- Eliminar Alumno")
    print("1.- Ver listado del Curso")
    print("1.- Salir")
    opcion = input("Seleccione una opcion: ")
    return int(opcion)

while True:
    opcion = menu()
    if opcion == 1:
        print("Hola")
    elif opcion == 2:
        print("Bolas")
    elif opcion == 3:
        print("Asies")
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción errónea. Intente de nuevo por favor.")