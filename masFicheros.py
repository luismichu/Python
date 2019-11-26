import os

fich = 'test.txt'
with open(fich, 'w') as file:
	file.write('resta\n')
	file.write('suma\n')
	file.write('division\n')
	file.write('mult\n')

with open(fich, 'r') as file:
	file.seek(0)
	print([linea[:-1] for linea in file])

def suma():
	print('hola')

locals()['suma']()