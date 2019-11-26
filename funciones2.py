def igual(lista1, lista2):
	encontrados = []
	flag = False
	for elem in lista1:
		if elem in lista2:
			flag = True
			encontrados.append(elem)

	if encontrados:
		return flag, encontrados
	else: 
		return flag

print(igual([1,2,3], [4,5,6]))