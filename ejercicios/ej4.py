x = {0, 1, 2, 12, 3, 4, 5, 6, 12}
lista = list(x) #el conjunto se convierte a lista

#se comprueba en la lista si el numero es para y si no lo es
#se remueve del conjunto
for num in lista:
    if num%2 == 0:
        x.remove(num)
        
print(x)