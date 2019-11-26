paises = ['argentina', 'españa', 'brasil']
poblacion = [40000000, 46000000, 190000000]

dic = dict(zip(paises, poblacion))

print(dic)

vocales = ['a', 'e', 'i', 'o', 'u']
nombres = ['ana', 'elena', 'isla', 'oscar', 'puerta', 'zara', 'alba']

print({vocal : [nombre for nombre in nombres if nombre.startswith(vocal)] for vocal in vocales})

cad = 'El gato con botas es amigo del gato tom'
print({palabra :  cad.count(palabra) for palabra in cad.split()})