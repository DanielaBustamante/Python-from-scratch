"""
EJERCICIO 4

Pedir dos numero al usuario y hacer todas las operaciones
basicas de una calculadora y mostrarlo por pantalla

"""

print("***************Calculadora*****************")

numero1 = int(input("Ingrese el primer numero: "))

numero2 = int(input("Ingrese el segundo numero: "))

resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
resto = numero1 % numero2

print(f"La resta es: {resta}")

print(f"La suma es: {numero1 + numero2}")

print("La multiplicacion es:", multiplicacion)

print("La division es:", division)

print("El resto de la division es:", resto)

"""
Otra forma de escribir el print puede ser
print("suma: " + str(numero1+numero2))
Y asi con el resto de operaciones
"""
