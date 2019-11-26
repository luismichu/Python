def del_reves(texto):
	return texto[::-1]

def num_espacios(texto):
	return texto.count(' ')

def num_carac_num(texto):
	num, carac = 0, 0
	for car in texto:
		if car.isnumeric():
			num += 1
		elif car.isalpha():
			carac += 1

	return carac, num


texto = 'Maria Rosa de las Mercedes'
print(texto, 'al reves:')
print(del_reves(texto))

texto = 'Hola que tal'
print('\nNumero de espacios en:', texto)
print(num_espacios(texto))

texto = 'Fecha: 05/11/2019'
print('\nNumero de caracteres y numeros en:', texto)
carac, num = num_carac_num(texto)
print('Caracteres:', carac)
print('Numeros:', num)