cadena = 'aaaabbcdddfgghhjklm'
#transformo la cadena a set para que no haya valores repetidos
conjunto = set(cadena)

#por cada elemento cuenta las veces que aparece en la cadena
#si es mayor que dos suma uno al total
total = 0
for elem in conjunto:
    if cadena.count(elem) >=2:
        total += 1
        
print(total)