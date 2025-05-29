from emoji import emojize

print("----------------------------")
print(f"--- \u26BD Tienda Deportiva \u26BD ---")
print("----------------------------")

print("Cual es tu nombre y apellido?")
nombre = input()
print(f"Bienvenido {nombre}")

while True:
    print("")
    print("Que deseas hacer?")
    print("-1 Ver las camisas de los equipos disponibles de la tienda?")
    print("-2 Precio de las camisas?")
    print("-3 Comprar una camisa?")
    print("-4 Salir")
        
    nombres_equipos ={
          "Real Madrid:120€",
           "FC Barcelona:120€",
            "Manchester City:100€",
             "Liverpool FC:90€",
              "Inter de Milán:80€",
             "AC Milan:80€",
            "Bayern Múnich:75€",
           "Borussia Dortmund:70€",
          "Paris Saint-Germain (PSG):70€",
        "Olympique de Lyon:65€"
    }
    respuesta = int(input())
    
    precios =  15 
    
    inventario = {
            "Real Madrid:20",
           "FC Barcelona:20",
            "Manchester City:15",
             "Liverpool FC:15",
              "Inter de Milán:10",
             "AC Milan:10",
            "Bayern Múnich:12",
           "Borussia Dortmund:8",
          "Paris Saint-Germain (PSG):18",
        "Olympique de Lyon:7"
    }
         
    if respuesta == 1:
        for i in nombres_equipos:
            print(f"{i} ")
            
    elif respuesta == 2:
            print(f"Precio de la camisa {precios} €")        
    elif respuesta == 3: 
        print("Que camisas deseas comprar:")
        compra = input()
        print(f"Has comprado la camisa del {compra}")
    elif respuesta == 4:
        print("Saliendo")
        
        break     
        

