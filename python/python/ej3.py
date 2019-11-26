def cifrar(cadena, clave):
	cad_cifrada = ''
	flag = True
	for car in cadena:
		if flag:
			cad_cifrada += car
			flag = False
		else:
			cad_cifrada = car + cad_cifrada
			flag = True

	cad_ascii = [(ord(car) - 97 + clave)%26 + 97 if not car.isspace() else 32 for car in cad_cifrada]
	cad_cifrada = ':'.join([str(num) for num in cad_ascii])
	return cad_cifrada

def descifrar(cad_cifrada, clave):
	cad_ascii = cad_cifrada.split(':')
	cad_ascii = [(int(num) - 97 - clave +26)%26 + 97 if not num == '32' else 32 for num in cad_ascii]
	cad_cifrada = [chr(num) for num in cad_ascii]
	cad_descifrada = ''
	flag = True if len(cad_cifrada)%2 == 0 else False
	for car in cad_cifrada:
		if flag:
			cad_descifrada += cad_cifrada[0]
			cad_cifrada = cad_cifrada[1:]
			flag = False
		else:
			cad_descifrada += cad_cifrada[-1]
			cad_cifrada = cad_cifrada[:-1]
			flag = True

	return cad_descifrada[::-1]

cadena = input('Cadena a cifrar: ')
clave = 0
cad_cifrada = cifrar(cadena, clave)
print(cad_cifrada)

cad_descifrada = descifrar(cad_cifrada, clave)
print(cad_descifrada)