lista = [('ALGEBRA',3),('FISICA',1),('QUIMICA',2)]

d = dict()

for elem in lista:
    lista2 = [1,]                   #se añade 1 a la lista2
    for i in range(2, elem[1] + 1): #desde 2 hasta el numero mas 1
        lista2.append(i)            #se añade i a la lista
    d.update({elem[0]: lista2})     #se actualiza el diccionario con
                                    #el nombre y la lista2

print(d)