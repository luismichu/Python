tam = int(input('Número de paquetes a introducir: '))

numeros = []
media = 0
for i in range(0, tam):
    print((tam - i), 'restante(s)')
    numeros.append(int(input('Introduce el peso del paquete: ')))
    media += numeros[i]
    
numeros.sort()
media /= len(numeros)

print('Menor:', numeros[0])
print('Mayor:', numeros[-1])
print('Media:', media)