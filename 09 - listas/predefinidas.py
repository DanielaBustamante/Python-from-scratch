from pprint import pprint

cantantes = ['Taylor', 'Harry', 'Camila', 'Selena']
numeros = [1, 2, 5, 8, 3, 4]

# Ordenar una lista
print(numeros)
numeros.sort() # para ordenar
print(numeros)

# Añadir elementos a la lista
cantantes.append("Lali")
cantantes.insert(1, "Emilia")
print(cantantes)

#Eliminar elementos de una lista
cantantes.pop(2) 
cantantes.remove('Taylor')
print(cantantes)

# Dar la vuelta a una lista
numeros.reverse()
print(numeros)

# Buscar dentro de uns lista
print('Selena' in cantantes)

# Contar elementos
print(len(cantantes))

# Cuantas veces aparece un elemento
print(numeros.count(8))

# Conseguir indice
print(cantantes.index("Camila"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)