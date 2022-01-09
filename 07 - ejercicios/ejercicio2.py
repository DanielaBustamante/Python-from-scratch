"""
Ejercicio 2

Escribir un scrip que nos muestrre por pantalla 
todos los numero pares del 1 al 120

"""

contador = 2               # empieza en el numero 2 - 1er par

while contador <= 120:     # mientra el contador vaya hasta 120
    if contador % 2 == 0:  # si contador divid 2 tiene un resto exacto
        print(contador)    # imprimir el valor
    contador += 1          # prueba con los num contador + 1 hasta llegar a 120
     
     
"""

###### EJEMPLO 1 #####
for contador in range(1, 121):        # si los numero en ese rango
    if contador%2 == 0:               # son exactos
        print(f"{contador} es impar") # son pares
    else:                             # sino
        print(f"{contador} es impar") # impares


###### EJEMPLO 2 #####
contador = 1
for contador in range(1, 61):
    print(contador*2)


###### EJEMPLO 3 #####
for contador in range (2,121):
    if contador % 2 == 0:
        pares += ", " + str(contador)
    else:
        impares +=  ", " + str(contador)
 
print (pares)
print (impares)

"""