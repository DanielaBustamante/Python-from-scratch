"""
Hacer un programa que muestre todos los numeros impares
entre dos numeros que elija el usuario.
"""
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 < numero2:
    for contador in range(numero1, (numero2 + 1)):
        if contador % 2 != 0:
            print(contador)
        contador += 1

else:
    print("El numero 1 debe ser menor al numero 2")
