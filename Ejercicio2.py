# Escribir un programa que pregunte al usuario su nombre, edad, dirección y
# teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el
# mensaje “<nombre> tiene <edad> años, vive en <dirección> y su número de
# teléfono es <teléfono>”.
nombre = input("Escriba su nombre: ")
edad = input("Escriba su edad: ")
direccion = input("Escriba su direccion: ")
telefono = input("Escriba su telefono: ")
diccionario = {"nombre": nombre, "edad": edad, "direccion": direccion, 
               "telefono": telefono}
print(diccionario["nombre"], "tiene", diccionario["edad"], "años, vive en",
      diccionario["direccion"], "y su número de teléfono es",
      diccionario["telefono"])