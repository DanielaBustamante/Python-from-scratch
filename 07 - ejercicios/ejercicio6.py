"""
Ejercicio 6
Mostrar las tablas de multiplicar del 1 al 10
Con su correspondiente titulo y luego las multiplicaciones.
"""

for cabecera in range(1, 11):
    print("########################################")
    print(f"############# Tabla del {cabecera} #############")
    print("########################################")

    for numero in range(1, 11):
        print(f"{numero} x {cabecera} = {numero*cabecera}")

    print("\n")


"""
# Otra forma de hacerlo:

contador = 0
 
while contador <=11:
    contador += 1
    for numero_tabla in range(1,11):
        print(f"{contador} x {numero_tabla} = {contador * numero_tabla}")
        
    else:
        
        print(f"Tabla finalizada: {contador}")
        print(" ")
"""