# Operaciones entre conjuntos
set_a = {'uno', 'dos', 'cuatro'}
set_b = {'cinco', 'uno', 'tres'}

# Union conjuntos por método
set_c = set_a.union(set_b)
print(set_c)

# Union conjuntos por operador
print(set_a | set_b)

# Intersección de conjuntos por método
set_c = set_a.intersection(set_b)
print(set_c)

# Intersección de conjuntos por operador
print(set_a & set_b)

# Diferencia de conjuntos por método
set_c = set_a.difference(set_b)
print(set_c)

# Diferencia de conjuntos por operador
print(set_a - set_b)

# Diferencia simétrica de conjuntos por método
set_c = set_a.symmetric_difference(set_b)
print(set_c)

# Diferencia simétrica de conjuntos por operador
print(set_a ^ set_b)