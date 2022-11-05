set_countries = {'col', 'ven', 'per', 'par'}
size = len(set_countries)
print('Cantidad de elementos del conjunto', size)

# Buscar un elemento en el conjunto
print('Colombia esta en el conjunto ', 'col' in set_countries)
print('Brazil esta en el conjunto ', 'bra' in set_countries)

# Adicionar elemento al conjunto
set_countries.add('arg')
size = len(set_countries)
print('Cantidad de elementos del conjunto', size)
print(set_countries)

# Eliminar elemento del conjunto
set_countries.remove('col')
size = len(set_countries)
print('Cantidad de elementos del conjunto', size)
print(set_countries)

# Eliminar elemento del conjunto, sino existe no genera error
set_countries.discard('eeuu')
size = len(set_countries)
print('Cantidad de elementos del conjunto', size)
print(set_countries)

# Dejar el conjunto en vacio, sin elementos
set_countries.clear()
size = len(set_countries)
print('Cantidad de elementos del conjunto', size)
print(set_countries)