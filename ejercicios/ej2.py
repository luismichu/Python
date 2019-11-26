tupla = (1, 2, 3, 4)
valor = 2

#si encuentra el valor en la tupla
if valor in tupla:
    #concatena la tupla desde el principio hasta la posición del valor y
    #desde la próxima posición del valor hasta el final
    tupla_sin_valor = tupla[:tupla.index(valor)] + tupla[tupla.index(valor) + 1:]
    print(tupla_sin_valor)
else:
    print('El valor', valor, 'no se encuentra en la tupla')