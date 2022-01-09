"""
Ejercicio 3

Escribir un programa que muestre los cuadrados 
(un num multiplicado por si mismo) de los 60
primeros numeros naturales.

RESOLVERLO CON EL BUCLE FOR Y WHILE

"""

print("########### Con FOR ##########")

for contador in range(1, 61):
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")



print("\n########### Con WHILE ##########")

contador = 0 

while contador <=60:
   
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    
    contador += 1
