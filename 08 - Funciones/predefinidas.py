nombre = "Dani"

print(type(nombre)) # nos da el tipo de dato

# Detectar el tipado
comprobar = isinstance(nombre, str) # compruebo si la variable es un str

if comprobar: # si no le pongo ningun operador de comparacion entiende que es true
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

# Limpiar espacios
frase = "   mi contenido   " 
print(frase) # la variable anterior conespacio
print(frase.strip()) # la variable sin espacio

"""
# eliminar variables
year = 2022
print(year)
del year # para borrar la variable escrita
print(year)
"""

# Comprobar variable vacia
texto = "  ff  "
if len(texto) <= 0: # comprueba la cantidad de caracteres que tiene
    print("La variable esta vacia") # si no hay nada mostra vacia
else: # sino mostrar la cantidad
    print("La variable tiene contenido: ", len(texto))

# Encontrar caracteres
frase = "La vida es bella"
print("El caracter se encuentra en la posicion: ")
print(frase.find("vida")) # busca esa palabra

# Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto") # primero lo que quiero sustiruir, luego lo que voy a sustituir
print(nueva_frase)

# Mayusculas y minusculas
print(nombre)
print(nombre.lower()) # para minuscula
print(nombre.upper()) # para mayuscula
