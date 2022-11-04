dict = {}
for x in range(1, 5):
  dict[x] = x * 2
print(dict)  

# Lo anterior en sintáxis corta
dict_v2 = {x : x * 2 for x in range(1, 5)}
print(dict_v2)

# Propiedades clave / valor
# Version 1
import random
paises = ['col', 'bol', 'arg', 'chi']
poblacion = {}
for pais in paises:
  poblacion[pais] = random.randint(1, 250)
print(poblacion)

# Propiedades clave / valor
# Version 2 - corta
poblacion_v2 =  {pais: random.randint(1, 250) for pais in paises}
print(poblacion_v2)

# Unir listas con tupla
nombres = ['nico', 'zule', 'santi']
edades = [12, 56, 98]
print(list(zip(nombres, edades)))

# Unir listas con tupla
# Version 2
dict_v2 = {nombre: edad for (nombre, edad) in zip(nombres, edades)}
print(dict_v2)
