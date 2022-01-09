"""

Condicional IF

SI se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones

"""

# Ejemplo 1

print("########## Ejemplo 1 ##########")

color  = input("Adivina mi color favortito: ")

if color == "rojo":
    print("Perfecto!!")
    print("El color es ROJO")
else:
    print("Color incorrecto!!")     

""""
Operadores de comparacion

== igual
!= diferente
< menor que 
> mayor que
<= menor o igual que 
>= mayor o igual que

"""

# Ejemplo 2

print("\n########## Ejemplo 2 ##########")

# year = 2020
year = int(input("¿En que año estamos?"))

if year >= 2021:
    print("Estamos de 2021 en adelante!!")
else:
    print("Es un  año anterior a 2021")

# Ejemplo 3

print("\n########## Ejemplo 3 ##########")

nombre = "Dani Bust"
ciudad = "buenos aires"
continente = "america"
edad = 19
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad!")

    if continente != "america":
        print("El usuario NO es americano")
    else:
        print(f"Es americano y de {ciudad}")

else:
    print(f"{nombre} NO es mayor de edad")

# Ejemplo 4

print("\n########## Ejemplo 4 ##########")

dia = int(input("Introduce el numero del dia de la semana: "))

"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    print("Es fin de semana")
"""

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6:
    print("Es sabado")
elif dia == 7:
    print("Es domingo")
else:
    print("Ingrese un numero del 1 al 7")

# Ejemplo 5

print("\n########## Ejemplo 5 ##########")

edad_minima = 18
edad_maxima= 65
edad_oficial = int(input("¿Tienes edad de trabajar? Introduce tu edad: "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")

"""
# Operadores logicos

and significa y
or que significa o
! negacion
not significa no

"""

# Ejemplo 6

print("\n########## Ejemplo 6 ##########")

pais = "Rusia"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana!")
else:
    print(f"{pais} no es un pais de habla hispana :(")

# Ejemplo 7

print("\n########## Ejemplo 7 ##########")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un pais de habla hispana!")
else:
    print(f"{pais} es un pais de habla hispana :)")

# Ejemplo 8

print("\n########## Ejemplo 8 ##########")

pais = "USA"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un pais de habla hispana!")
else:
    print(f"{pais} es un pais de habla hispana :)")
