# Escribir un programa que guarde en una variable el diccionario
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y
# muestre su símbolo o un mensaje de aviso si la divisa no está en
# el diccionario.
diccionario = {"Euro":"€", "Dollar":"$", "Yen":"¥"}
divisa = input("Escriba una divisa (Euro, dollar, yen): ").capitalize()
if divisa in diccionario:
    print("La divisa es: " + diccionario[divisa])
else:
    print("Error, la divisa no esta en el diccionario")