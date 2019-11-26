import collections

lista1 = [0, 1, -1, 1, 1, 1 ,-1, -1, 1]
lista2 = []

win = [[1, 1, 1, 0, 0, 0, 0, 0, 0],
	   [0, 0, 0, 1, 1, 1, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 1, 1, 1]]

for i in range(len(win)):
	lista2 = [lista1[j] * win[i][j] for j in range(len(lista1))]
	print(lista2, win[i])
	
	if lista2 == win[i]:
		print('Encontrado')
		break



def ganador(lista):
	
	