#MARTIN PAVEZ   
#EVALUACION FORMATIVA 2 "MENU SUSHI"



rolls = ["Pikachu Roll", "Otaku Roll", "Pulpo Venenoso Roll", "Anguila Electrica Roll"]
precios = [4500, 5000, 5200, 4800]
unidades = [0,0,0,0]


ciclo = True
print("Bienvenido al Sushi Anime")
while ciclo == True:
    try:
        opcion = int(input(f"Seleccione el roll que desee o presione '0' para salir:\n1.{rolls[0]} ${precios[0]}\n2.{rolls[1]} ${precios[1]}\n3.{rolls[2]} ${precios[2]}\n4.{rolls[3]} ${precios[3]}\n"))
    except ValueError:
        print("Error de seleccion")
    else:
        if opcion == 0:
            pass
        elif opcion == 1:   
            unidades[0] +=1 
        elif opcion == 2:
            unidades[1] +=1
        elif opcion == 3:
            unidades[2] +=1
        elif opcion == 4:
            unidades[3] +=1
        else:
            print("Opcion invalida")

        total = unidades[0]*precios[0] + unidades[1]*precios[1] + unidades[2]*precios[2] + unidades[3]*precios[3] 
        print("Pedido:")
        print(f"{unidades[0]}x {rolls[0]}\n{unidades[1]}x {rolls[1]}\n{unidades[2]}x {rolls[2]}\n{unidades[3]}x {rolls[3]}")
        print(f"Total: ${total}")
        while opcion == 0:
            codigo_descuento = input("Ingrese un codigo de descuento\nPresione 'x' para volver a pedir\nPresione 0 para terminar")
            if codigo_descuento == "soyotaku":
                descuento = total*0.1


            

#Codigo incompleto.