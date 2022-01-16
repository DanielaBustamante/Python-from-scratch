"""
# Funciones:
Una funcion es un conjunto de instrucciones agrupadas bajo 
un nombre concreto que pueden reutilizarse invocando a la 
funcion tantas veces como sea necesario.

def nombreDeMiFuncion(parametros):
    # Bloque / Conjunto de instrucciones

nombreDeMiFuncion(mi_parametro)

"""

"""
# Ejemplo 1
print("\n###### Ejemplo 1 ######")

# Definir funcion
def muestraNombre():
    print("Victor")
    print("Daniel")  
    print("Juan")    
    print("Francisco")  
    print("Rocio")
    print("Gustavo")
    print("\n")

# Invocar funcion
muestraNombre()
muestraNombre()
muestraNombre()


# Ejemplo 2
print("\n###### Ejemplo 2 ######")

def muestraNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
muestraNombre(nombre, edad)


# Ejemplo 3
print("\n###### Ejemplo 3 ######")
def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range(1, 11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")

tabla(3)
tabla(12)


# Ejemplo 3.1
print("\n---------------------------------------------------")
for numero_tabla in range(1, 11):
    tabla(numero_tabla)


# Ejemplo 4

print("\n###### Ejemplo 4 ######")

# Parametros opcionales

def getEmpleado(nombre, dni = False): #para que el dni sea opcional
    # se puede usar false o none para que sea opcional
    print("Empleado")
    print(f"Nombre: {nombre}")

    if dni != False: # si es distitnto a false muestro el dni
        print(f"DNI: {dni}")

getEmpleado("Dani") # no esta el dni 


# Ejemplo 5

# parametro opcionales y return o devolver datos

print("\n###### Ejemplo 5 ######")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("Dani"))


# Ejemplo 6

# parametro opcionales y return o devolver datos

print("\n###### Ejemplo 6 ######")

def calculadora(numero1, numero2, basicas = False):
    resta = numero1 - numero2
    suma = numero1 + numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"

        cadena += "Resta: " + str(resta)
        cadena += "\n"

    else:
        cadena += "Multiplicacion: " + str(multiplicacion)
        cadena += "\n"
        
        cadena += "Division: " + str(division)
        cadena += "\n"

    return cadena

print(calculadora(5, 5, True))

def new_func(resta, suma, cadena):
    cadena += "Suma: " + str(suma)
    cadena += "\n"

    cadena += "Resta: " + str(resta)
    cadena += "\n"
"""


# Ejemplo 7

print("\n###### Ejemplo 7 ######")