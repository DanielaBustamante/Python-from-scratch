"""
Ejercicio 10.
El programa tiene que pedir la nota de 15 alumnos y sacar
por pantalla cuantos han aprobado y cuantos han suspendido.
"""

contador = 1
aprobados = 0
desaprobados = 0

numeros_alumnos = int(input("¿Cuantos alumnos tienes?: "))

while contador <= numeros_alumnos:
    nota = int(input(f"¿Que nota quieres ponerle al \"alumno{contador}\"? "))

    if nota >= 7:
        aprobados += 1
    
    else:
        desaprobados += 1
    
    contador += 1

print(f"\nAlumnos aprobados: {aprobados}")

print(f"Alumnos desaprobados: {desaprobados}")
