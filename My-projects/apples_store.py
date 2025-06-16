print("********* Bienvenido a **********")
print("*** - - Tienda de Manzanas -- ***")
print("*********************************")

print("Cual es tu nombre?")
nombre = input()
print("Bienvenido!", nombre)

manzanas_rojas = 20
manzanas_verdes = 20
total_manzanas = 40
precio = 5

print("Actualmente tenemos:")
print(manzanas_rojas,"Manzanas Rojas")
print(manzanas_verdes,"Manzanas verdes")
print("Precio por unidad",precio,"€")

print("Cuantas mazanas deseas")
compra = int(input())
print("Color de la Manzana?")
color = input()
total = int(compra * precio)


print(nombre,"Has comprado",compra,"Manzanas")
print("Color",color)
print("Total",total,"€")

print("Manzanas disponibles:",total_manzanas - compra)

