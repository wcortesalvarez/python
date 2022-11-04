import random
paises = ['col', 'bol', 'arg', 'chi']
# Propiedades clave / valor
# Version corta
poblacion_v2 =  {pais: random.randint(1, 250) for pais in paises}
print(poblacion_v2)

# Lo angerior pero con condicional para filtro
resultado = {pais : poblacion for (pais, poblacion) in poblacion_v2.items() if poblacion > 100}
print(resultado)

# Generar diccionario
# con condicional para un texto para solo vocales
# se convierte a mayúscula pero sin repetir vocal
texto = 'ciudad de Pereira'
vocales_unicas = {v: v.upper() for v in texto if v in ('aeiou')}
print(vocales_unicas)
