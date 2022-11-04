# Crear lista de números por ciclo repetitivo
numeros = []
for elemento in range (1, 10):
  print('adicionando: ', elemento)
  numeros.append(elemento)
print(numeros)

# Crear lista de números de manera directa
# con list comprehension
numeros_v2 = [elemento for elemento in range(1, 10)]
print(numeros_v2)

# Agregar lista de números pares multiplicado por 5
numeros = []
for elemento in range (1, 10):
  if elemento % 2 == 0:
    numeros.append(elemento * 5)
print('numeros pares por 5: ', numeros)

# Agregar lista de números pares multiplicado por 5
# con list comprehension
numeros_v2 = [elemento * 5 for elemento in range(1, 10) if elemento % 2 == 0]
print(numeros_v2)
