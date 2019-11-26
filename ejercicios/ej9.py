dic = {123: ('Juan', 26), 234: ('María', 25), 345: ('José', 22)}

lista = []
#se cogen solo los valores sin clave
for elem in dic.values():
    lista.append(list(elem)[0]) #se guarda el primer elemento de los valores
    
print(lista)