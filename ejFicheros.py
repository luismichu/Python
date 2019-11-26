import os

carpeta = 'ejercicioFicheros'
os.chdir('C:/Users/AlumnoT/Desktop')

if not carpeta in os.listdir():
	os.makedirs(carpeta)

os.chdir(carpeta)

with open('palabras.txt', 'w') as file:
	for i in range(3, 0, -1):
		file.write(input('Introduce ' + str(i) + ' palabras: ') + '\n')

with open('palabras.txt', 'r') as file:
	print([line for line in file])