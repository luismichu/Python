n=327387725427

tupla = tuple(str(n))
#igual que en el ejercicio 6, se añade el elemento
#del conjunto con su numero de veces que aparece,
#pero en un diccionario
dic = dict()
for elem in set(tupla):
    dic.update({int(elem): tupla.count(elem)})

print(dic)