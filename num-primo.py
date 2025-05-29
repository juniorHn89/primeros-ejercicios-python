# pedir usuario que ingrese un Numero
print("Ingresa un numero:")

N = int(input())

for num in range(1,N + 1):
    if num > 1: # Verificar si el numero es primo > 1
       es_primo = True
       for i in range(2,num):
            if num % i == 0:
                es_primo = False 
                break
       if es_primo:
            print(f"El numero {num} es primo") 