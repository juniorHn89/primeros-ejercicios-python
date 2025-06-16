# Sumar números del 1 al N

# Pedir al usuario que ingrese un numero!

print("Ingresa un numero:")
n = int(input())
suma = 0

for i in range(1,n+1):
    suma+=i
    
print("La suma del 1 hasta ", n, "es:", suma)    
    