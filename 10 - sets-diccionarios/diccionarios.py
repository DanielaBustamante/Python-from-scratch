"""
Diccionario: Un tipo de dato que almacena un  conjunto de datos.
en formato clave > valor.
Es parecido a un array asociativo o un objeto json.
"""

persona = {
    "nombre": "dani",
    "apellido": "bustamante",
    "linkedin": "https://www.linkedin.com/in/daniela-annabella-bustamante"
}

print(persona["linkedin"])

# Lista con duccionarios

contactos = [
    {
        'nombre': 'dani',
        'email': 'daniela.annabella05@gmail.com'
    },
    {
        'nombre': 'ana',
        'email': 'anabella08@gmail.com'
    },
    {
        'nombre': 'vanesa',
        'email': 'vene123@gmail.com'
    }
]

contactos[0]['nombre'] = "Dalila" # le cambia el valor a esa propiedad

print(contactos[0]['nombre']) # entro al indice principal y luego al indice de texto

print("\nListado de contactos: ")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("--------------------------------------------------------------")