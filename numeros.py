'''
crear programa con menu inicial que nos preguntara si queremos crear carpeta o archivo.
1. Crear carpeta llamada biblioteca
2. Entrar en la carpeta
3. Comprobar si existe archivo 'archivo200'
4. Si no existe se crea y se introduce una lista de 20 num entre -20 y 20
5. Abrir archivo y decir mayor, menor y media
6. Introducir una palabra, extraer suma y llamar a la funcion
'''
import os, random

def suma():
	print('Se ha llamado a la funcion suma\n')

while True:
	print('1. Crear carpeta')
	print('2. Crear archivo')
	print('3. Buscar archivo archivo200 en carpeta biblioteca')
	print('4. LLamar a suma')
	print('5. Salir')
	opcion = int(input('Opcion: '))

	if opcion == 1:
		carpeta = input('Nombre de la carpeta: ')
		if carpeta in os.listdir():
			print('Error. Carpeta ya existe')
		else:
			os.makedirs(carpeta)
			print('Carpeta', carpeta, 'creada\n')

	elif opcion == 2:
		archivo = input('Nombre del archivo: ')
		if archivo in os.listdir():
			print('Error. El archivo ya existe\n')
		else:
			with open(archivo, 'w') as file:
				print('Archivo creado\n')

	elif opcion == 3:
		carpeta = 'biblioteca'
		archivo = 'archivo200'
		if not carpeta in os.listdir():
			os.makedirs(carpeta)
			
		os.chdir(carpeta)	
		if not archivo in os.listdir():
			with open(archivo, 'w') as file:
				for i in range(20):
					file.write(str(random.randint(-20, 21)) + '\n')

		with open(archivo, 'r') as file:
			numeros = [int(line) for line in file]

		numeros.sort()
		print('Valor maximo:', numeros[-1])
		print('Valor minimo:', numeros[0])
		print('Media:', sum(numeros) / len(numeros), '\n')

		os.chdir('..')

	elif opcion == 4:
		with open('test.txt', 'r') as file:
			lista = [linea[:-1] for linea in file]

		indice = lista.index('suma')
		if indice != -1:
			locals()[lista[indice]]()

	elif opcion == 5:
		break
	else:
		print('\nOpcion no valida')