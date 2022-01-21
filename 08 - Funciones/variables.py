"""
VARIABLES LOCALES: Se definen dentro de la funcion y no se ouede usar
fuera de ella, solo estan disponibles dentro. A no ser que hagamos un
return.

VARIABLES GLOBALES: Son las que se declaran fuera de una funcion y
estan disponibles dentro y fuera de ellas.
"""


frase = "Nothing's impossible" # global

print(frase)

def holaMundo():
    frase = "Hello World!" # local
    print("Dentro de la funcion: ")
    print(frase)

    year = 2021 # local, si la llamara fuera no la mostraria
    print(year)


    global LinkeIn # hago que una variable local pase a ser global tambien

    LinkeIn = "www.linkedin.com/in/daniela-annabella-bustamante"

    print("Dentro: ", LinkeIn)

    return "Dato devuelto " + str(year)

print(holaMundo()) # imprimo todo lo que este dentro de la funcion

print("Fuera: ", LinkeIn)
