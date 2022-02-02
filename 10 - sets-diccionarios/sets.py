"""
SET es un tipo de dato para tener una coleccion de valores,
pero no tiene ni indice ni orden
"""

personas = {
    "dani",
    "rocio",
    "pilar"
} # al imprimirlo lo muestra en cualquier orden

personas.add("fran") # para agregar
personas.remove("rocio")

print(type(personas))
print(personas)
