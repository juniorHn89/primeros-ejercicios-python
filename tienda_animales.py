print("********* Bienvenido a **********")
print("*** - - Tienda de Manzanas -- ***")
print("*********************************")

print("Cual es tu nombre?")
nombre = input()
print("Bienvenido!", nombre)
while True:

    print("Selecciona la opcion que deseas:")
    print("-1 * Conocer los Animales de la Tienda ")
    print("-2 * Comprar un Animal ")
    print("-3 * Salir ")

    respuesta = int(input())
    
    perros = 25
    gatos =  20
    loros =  10
    total_animales = 55

    if respuesta == 1:
        print("Tenemos",perros,"perros")
        print("Tenemos", gatos, "perros")
        print("Tenemos", loros, "perros")
        print("Tenemos", total_animales,"animales en total!")
            

    elif respuesta == 2:
        print("Que animal deseas comprar?")
        compra = input()
        print("has comprado un",compra)

    elif respuesta == 3:
        print("Sesion Cerrada!")
    break
print("Saliendo del programa....")

