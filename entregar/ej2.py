print('Introduce 5 numeros')
lista = [int(input()) for i in range(5)]

lista2 = [num if num >= 0 else num * -1 for num in lista]
lista = [num for num in lista if num >= 0]

print(lista)
print(lista2)