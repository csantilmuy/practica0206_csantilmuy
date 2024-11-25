# Escribir un programa que cree un diccionario vacío y lo vaya llenado con
# información sobre una persona (por ejemplo nombre, edad, sexo, teléfono,
# correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada
# un nuevo dato debe imprimirse el contenido del diccionario.
# Crear un diccionario vacío
persona = {}
while True:
    clave = input("¿Qué información quieres añadir? (por ejemplo, nombre, edad, sexo, etc.): ")
    valor = input(f"Ingrese el/la {clave}: ")
    persona[clave] = valor
    print("Información actualizada de la persona:")
    for key, value in persona.items():
        print(f"{key}: {value}")
    continuar = input("¿Desea añadir más información? (sí/no): ").lower()
    if continuar != "sí":
        break
print("Datos finales de la persona:")
for key, value in persona.items():
    print(f"{key}: {value}")
