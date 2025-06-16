print("***********************")
print("*** Mini Calculadora ***")
print("***********************")

print("Que operacion desas hacer?")
print("-1 Sumar")
print("-2 Restar")
print("-3 Multiplicar")

respuesta = int(input())

if respuesta == 1:
    print("Ingresa el numero:")
    num1 = int(input())
    print("Ingresa el otro numero:")
    num2 = int(input())
    resultado = num1 + num2
    print(f"El resultado de la suma es : {resultado}")
    
    
    
