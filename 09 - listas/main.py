"""
LISTAS (arrays)
Son coleciones o conjuntos de datos/valores,
bajo un unico nombre.
Para acceder a esos valores podemos usar un
indice numerico.
"""

# Definir listas
pelicula = "batman"
peliculas = ["batman", "spiderman", "el señor de los anillos"]
cantantes = list(('Taylor', 'Harry', 'Camila')) 
# hay que pasarle una tupla para que lo reconozca
years = list(range(2020, 2050))
variada = ["dani", 30, 4.4, True, "Texto"]

print(peliculas)
print(cantantes)
print(years)
print(variada)

# Indices
pelicula = "Otra cosa" # Reasignar variables
peliculas[1] = "Gran Torino" # Modificamos el indice de la lista

print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:1]) # saca de taylor al inicio del otro
print(peliculas[1:]) # saca a partir del 1

# Añadir elementos a lista
cantantes.append("Selena")
cantantes.append("Lali")
print(cantantes)

# Recorrer lista
nueva_pelicula = ""
while nueva_pelicula != "parar": # cuando es distinto de parar poner una peli
    nueva_pelicula = input("Introduce una nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n**** LISTADOS PELICULAS *****")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}") 
# mostrar el num de la pelicula y luego la pelicula

# Lista multidimensional
print("\n**** Listado de contactos *****")
contactos = [
    [
        'daniela',
        'daniela.annabella05@gmail.com'        
    ],
    [
        'antonio',
        'antonio897@hotmail.com'
    ],
    [
        'luis',
        'luis17@outlook.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")