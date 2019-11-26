lista = []
#mientras que se reciba una entrada se repite el bucle
while True:
    num = input('Escribe un número (en blanco para salir): ')
    if num == '':
        break
    else:
        lista.append(int(num))
        
#la lista se pasa a conjunto para no tener números repetidos
conjunto = set(lista)
lista_num_repes = []
#para todos los elementos del conjunto se añade una tupla de dos
#valores, el elemento y el número de veces que aparece
for elemento in conjunto:
    lista_num_repes.append((elemento, lista.count(elemento)))
    
print(lista_num_repes)