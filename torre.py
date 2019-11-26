palo1 = [3,2,1]
palo2 = []
palo3 = []
paloBueno = palo1.copy()

def movimiento(palo1, palo2, palo3):
	if len(palo1) > 0:
		if len(palo3) == 0:
			palo3.append(palo1.pop(-1))
		elif len(palo2) == 0:
			if len(palo3) > 1:
				palo3.append(palo1.pop(-1))
			else:
				palo2.append(palo1.pop(-1))
		else:
			palo2Copy = palo2.copy()
			palo2Copy.append(palo3[0])
			palo2CopySort = palo2Copy.copy()
			palo2CopySort.sort()
			palo2CopySort.reverse()
			if palo2Copy == palo2CopySort:
				palo2.append(palo3.pop(-1))
			else:
				palo3.append(palo2.pop(-1))
	else:
		if len(palo2) > 1:
			palo1.append(palo2.pop(-1))

print('', ['*'*num for num in palo1], '\n', ['*'*num for num in palo2], '\n', ['*'*num for num in palo3], '\n')
while palo3 != paloBueno:
	movimiento(palo1, palo2, palo3)
	print('', ['*'*num for num in palo1], '\n', ['*'*num for num in palo2], '\n', ['*'*num for num in palo3], '\n')
