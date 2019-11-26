from random import randint

max_num = int(input('Hasta que numero quieres adivinar: '))
intentos = int(input('Numero de intentos: '))

adivinar = randint(0, max_num)

num = input('\nAdivina: ')
if num.isnumeric():
	intento = 1
	dic = {intento:int(num)}
	while intento < intentos and num.isnumeric() and int(num) != adivinar:
		print('Casi. Te quedan', (intentos - intento), 'intentos')
		print(dic)	

		num = input('\nAdivina: ')
		intento += 1
		if num.isnumeric(): dic.update({intento:int(num)})

	if num.isnumeric() and int(num) == adivinar:
		print('\nEnhorabuena!! Has acertado')
		print(dic)
	else:
		print('\nSe quedo en el casi')
		print('Numero no adivinado:', adivinar)
		print(dic)

else:
	print('\nSe quedo en el casi')
	print('Numero no adivinado:', adivinar)