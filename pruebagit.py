print('"Bienvenido a Bibliografia"')
print(' Selecciona una opcion:')


testamento = input('1- Antiguo Testamento \n2- Nuevo Testamento\n')

pregunta_1 = None


if testamento == '1':
    print('Has elejido el Antiguo Testamento.\n')
    pregunta_1 =input('Cuantos libros tiene el A.T?\n')
    if pregunta_1 == '39':
        print('Correcto!!')
    pregunta_1 =input('Nombres de los Profetas Mayores?\n')
    if pregunta_1 == 'Daniel Jeremias Isaias Ezequiel':
        print('Excelente')

    
    
elif testamento == '2':
    print('Has elejido el Nuevo Testamento')
    pregunta_2 =input('Cuantos libros tiene el N:T?\n')
if pregunta_2 == '27': 
    print('Correcto!!')
    
    
else:
    print('Respuesta Incorrecta')

