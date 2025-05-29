# Pedir al usuario un numero
respuesta = int(input("Ingresa el numero secreto:"))
# Crear Bucle
while True:
    # Generar un número secreto entre 1 y 100
    num_secreto = 50

    # Definir número de intentos máximos (5)
    intentos = 5
    # Inicializar contador de intentos en 0
    contador = 0
    #Aumentar el contador de intentos
    contador = +1
    # Si el número del usuario es mayor que el número secreto:
    #        Mostrar "Demasiado alto"
    if respuesta > num_secreto:
        print("Demasiado Alto")
    #Si  es menor:Mostrar "Demasiado Bajo"
    elif respuesta < num_secreto:
        print("Demasiado bajo")
    # Si no:Mostrar "¡Correcto!" y salir del bucle
    else:
        print("Correcto Adivinastes eres un Crack!!")
    break    
  
            

    # Si el usuario no adivinó después de 5 intentos:
    # Mostrar "Se acabaron los intentos. El número era: [número_secreto]"
