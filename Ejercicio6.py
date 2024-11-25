# Escribir un programa que permita gestionar la base de datos de alumnado de
# un classroom. Los alumnos y alumnas se guardarán en una lista que almacena
# un diccionario para cada alumno/a en el que la clave de cada alumno/a será
# su NIF, y el valor será otro diccionario con los datos del alumno/a (nombre,
# apellidos, teléfono, correo, aprobado), donde aprobado tendrá el valor True
# si ha aprobado el módulo. El programa debe preguntar al usuario por una
# opción del siguiente menú: (1) Añadir alumno/a, (2) Eliminar alumno/a,
# (3) Mostrar alumno/a, (4) Listar todo el alumnado, (5) Listar alumnado
# aprobado, (6) Terminar. En función de la opción elegida el programa tendrá
# que hacer lo siguiente:
# (1) Preguntar los datos del alumno/a, crear un diccionario con los datos y
# añadirlo a la base de datos.
# (2) Preguntar por el NIF del alumno/a y eliminar sus datos de la base
# de datos.
# (3) Preguntar por el NIF del alumno/a y mostrar sus datos.
# (4) Mostrar lista de todo el alumnado de la base de datos con su NIF y nombre
# (5) Mostrar la lista del alumnado aprobado de la base de datos con su NIF
# y nombre.
# (6) Terminar el programa.
base_datos = {}
def mostrar_menu():
    print("\nMenú:")
    print("1. Añadir alumno/a")
    print("2. Eliminar alumno/a")
    print("3. Mostrar alumno/a")
    print("4. Listar todo el alumnado")
    print("5. Listar alumnado aprobado")
    print("6. Terminar")
def anadir_alumno():
    nif = input("Introduce el NIF del alumno/a: ")
    if nif in base_datos:
        print("El NIF ya existe, intenta con otro")
        return
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    telefono = input("Introduce el teléfono: ")
    correo = input("Introduce el correo electrónico: ")