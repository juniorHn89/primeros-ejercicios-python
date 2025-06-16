
# Comprobar si la palabra es paliondromo
# Ejercicio creado por IA "Deepseek"    
palabra = "ana"
es_palindromo = True

for i in range(len(palabra) // 2):
    if palabra[i] != palabra[-i - 1]:  # ¡Esta es la línea clave!
        es_palindromo = False
        break
    
print(f"La palabra es palindromo {es_palindromo}")