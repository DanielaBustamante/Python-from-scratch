"""
Una variables es un contenedor de informacion
que dentrro guardara un dato, se pueden crear 
muchas variables y que cada una tenga un dato distinto
"""

# crear variables y asignarles un valor   
texto = "Master en Python"
texto2 = "con tutor"
num = 45
decimal = 6.7

#mostrar valoreres de las variables
print(texto)
print(texto2)
print(num)
print(decimal)

#sustituir el valor de algunas variables / reasignando valores
print("-----------------------------------------------------")

num = 77
decimal = 8.9
print(num)
print(decimal)

# Concatenacion
nombre = "Daniela"
apellido = "Bustamante"
web = "linkedin.com/in/daniela-annabella-bustamante"

print(nombre + " " + apellido + " - " + web)
print(f"{nombre} {apellido} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellido, web))
