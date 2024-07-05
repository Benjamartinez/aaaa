import os 
import csv

filename = 'Alumnos.csv'

def menu():
    print("1.- Ingresar Alumno")
    print("2.- Eliminar Alumno")
    print("3.- Ver listado del Curso")
    print("4.- Salir")
    opcion = input("Seleccione una opcion: ")
    return int(opcion)

def rut_existe(rut):
  
     with open (filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == rut:
                return True

def ingresar_alumno():
    alumnos = filename
    rut = input("Ingrese el RUT del alumno: ")

    if rut_existe(rut):
        print("\nEl RUT ingresado ya existe. Intente con otro.")
        return

    nombre  = input("Ingrese el NOMBRE del alumno: ")
    nota = input("Ingrese la NOTA del alumno: ")

    file_exists = os.path.isfile(alumnos)

    with open(alumnos, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists or os.stat(filename).st_size == 0:
             writer.writerow(['Rut','Nombre','Nota'])
        writer.writerow([rut, nombre, nota])

    print(f"Alumno Ingresado con exito en {alumnos}")

def eliminar_alumno():
    rut = input("\nIngres el RUT del alumno que desea eliminar: ")
    if not rut_existe(rut):
        print("\nEl RUT ingresado no existe. Intente con otro RUT.")
        return
    
    with open(filename, mode='r') as file:
        rows = list(csv.reader(file))
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] != rut:
                writer.writerow
    print(f"\nAlumno con RUT {rut} eliminado exitosamente.")


def ver_listado():
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

while True:
    opcion = menu()
    if opcion == 1:
        ingresar_alumno()
    elif opcion == 2:
        eliminar_alumno()
    elif opcion == 3:
        ver_listado()
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción errónea. Intente de nuevo por favor.")