lista = [num for num in range(1, 15)]

[lista.remove(num) for num in lista if num%2==0]

print(lista)