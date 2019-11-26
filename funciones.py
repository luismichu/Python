def fun(lista):
	vocales = ['a', 'e', 'i', 'o', 'u']
	vocal = [elem for elem in lista if str(elem).isalpha() and elem in vocales]
	positivo = [elem for elem in lista if str(elem).isdigit() and elem >= 0]
	negativo = [elem for elem in lista if str(elem).startswith('-') and str(elem)[1:].isdigit() and elem < 0]
	par = [elem for elem in lista if str(elem).isdigit() and elem%2 == 0]
	par.extend([elem for elem in lista if str(elem).startswith('-') and str(elem)[1:].isdigit() and elem%2 == 0])
	impar = [elem for elem in lista if str(elem).isdigit() and elem%2 != 0]
	impar.extend([elem for elem in lista if str(elem).startswith('-') and str(elem)[1:].isdigit() and elem%2 != 0])
	return vocal, positivo, negativo, par, impar

lista = [1,2,-3, 'a', 'b', 'e', -4, 'c']

vocales, positivos, negativos, pares, impares = fun(lista)
print('Vocales:', vocales)
print('Positivos:', positivos)
print('Negativos:', negativos)
print('Pares:', pares)
print('Impares:', impares)