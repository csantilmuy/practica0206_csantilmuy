# Escribir un programa que cree un diccionario de traducción español-inglés.
# El usuario introducirá las palabras en español e inglés separadas por dos
# puntos, y cada par <palabra>:<traducción> separados por comas, hasta que el
# usuario introduzca la palabra “terminar”. El programa debe crear un
# diccionario con las palabras y sus traducciones. Después pedirá una frase
# en español y utilizará el diccionario para traducirla palabra a palabra.
# Si una palabra no está en el diccionario debe dejarla sin traducir.
traducciones = {}
print("Introduce las palabras en el formato <palabra>:<traducción> separadas por comas.")
print("Escribe 'terminar' para finalizar la entrada.")
entrada = input("Palabras (ejemplo: casa:house, perro:dog): ")
while entrada.lower() != "terminar":
    pares = entrada.split(",")
    for par in pares:
        if ":" in par:
            espanol, ingles = par.split(":")
            traducciones[espanol.strip()] = ingles.strip()
    print("Diccionario actual:")
    for esp, eng in traducciones.items():
        print(f"{esp} -> {eng}")
    entrada = input("Introduce más palabras o escribe 'terminar' para finalizar: ")
frase = input("Introduce una frase en español para traducir: ")
palabras = frase.split()
traduccion = []
for palabra in palabras:
    if palabra in traducciones:
        traduccion.append(traducciones[palabra])
    else:
        traduccion.append(palabra)
frase_traducida = " ".join(traduccion)
print("Frase traducida:", frase_traducida)