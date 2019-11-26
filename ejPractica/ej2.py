tam = int(input('Número de paquetes a introducir: '))

numeros, menor10, entre10y20, mayor20 = [], [], [], []

for i in range(0, tam):
    print((tam - i), 'restante(s)')
    numeros.append(int(input('Introduce el peso del paquete: ')))
    if numeros[i] < 10:
        menor10.append(numeros[i])
    else:
        if numeros[i] >= 10 and numeros[i] <= 20:
            entre10y20.append(numeros[i])
        else:
            mayor20.append(numeros[i])
        
print('Menores de 10kg:', menor10)
print('Entre 10kg y 20kg:', entre10y20)
print('Mayores de 20kg:', mayor20)