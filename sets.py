set_countries = {'col', 'ven', 'per'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 6, 23, 114}
print(set_numbers)

set_types = {16, 'hola', False, 19.12}
print(set_types)

# Crear conjunto a partir de un string
set_from_string = set('hola')
print(set_from_string)

# Conjunto con cadena de texto
# No muestra textos repetidos
set_from_tuples = set(('abc', 'def', 'xyz', 'abc'))
print(set_from_tuples)

# Números como lista de elementos
# Se convierten en un conjunto
# no se muestran números repetidos
numbers = [1, 2, 3, 4, 1, 2, 7, 23, 16, 12, 21]
set_numbers = set(numbers)
print(set_numbers)

# Retornar set (conjunto) a una lista
unique_numbers = list(set_numbers)
print(unique_numbers)