# Escribir un programa que guarde en un diccionario los precios de los
# artículos de la tabla, pregunte al usuario por un artículo, un número de
# unidades y muestre por pantalla el precio de esa cantidad de producto. Si el
# producto no está en el diccionario debe mostrar un mensaje
# informando de ello. 
# Producto_|_Precio
# Pan      | 1,40
# Huevos   | 2,30
# Cebolla  | 0,85
# Aceite   | 4,35
productos = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}
producto = input("Ingrese el nombre del producto que desea: ")
cantidad = input("Ingrese la cantidad que desea comprar: ")
if producto in productos:
    precio_unitario = productos[producto]
    precio_total = precio_unitario * int(cantidad)
    print(f"El precio de {cantidad} unidad(es) de {producto} es {precio_total:.2f}")
else:
    print("El producto ingresado no está disponible")
