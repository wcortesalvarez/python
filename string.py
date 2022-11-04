name = "Wilson"
last_name = "Cortes Alvarez"
full_name = name + " " + last_name
print(full_name)

print("Longitud del nombre completo ", len(full_name))

quote = "I'm Wilson"
print(quote)

quote2 = 'He said "Hello"'
print(quote2)

template = "Mi nombre es " + name + " mi apellido es " + last_name
print('version 1: ', template)

template = "Mi nombre es {} y mi apellido es {}".format(name, last_name)
print('version 2: ', template)

# La mas usa en Python
template = f"Mi nombre es {name} y mi apellido es {last_name}"
print('version 3: ', template)

