# Generar un número secreto entre 1 y 100
print("Adivina el numero secreto del 1 al 100!")
num_secreto = 15
print("")

while True:
# Repetir hasta que el usuario adivine el número
# Pedir al usuario que ingrese un número
    print("Cual crees que sea el numero oculto?")
    respuesta = int(input())

    # Si el número del usuario es mayor que el número secreto
    #        Mostrar "Demasiado alto"
    if respuesta > num_secreto:
        print("Ups! Demasiado Alto")
        print("Intentalo de Nuevo!")
        # Si el número del usuario es menor que el número secreto
    #       Mostrar "Demasiado bajo"
    if respuesta < num_secreto:
            print("Estas cerca")
            print("Intentalo de Nuevo!")
    
    elif respuesta == num_secreto:
        print("Felicidades adivinastes el numero!!")
        break