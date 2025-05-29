lista = []

for i in range(5):
    num = int(input(f"Ingrese el número {i + 1}: "))
    lista.append(num)

print("Números ingresados:", lista)

mayores = 0
for i in lista:
    if i > 10:
        mayores += 1

print("Números mayores que 10:", mayores)
