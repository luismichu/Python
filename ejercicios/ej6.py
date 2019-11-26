n=327387725427

tupla = tuple(str(n))
#se añade a la lista el elemento y el numero de veces que aparece
#en forma de tupla
lista = []
for elem in set(tupla):
    lista.append((int(elem), tupla.count(elem)))

print(lista)