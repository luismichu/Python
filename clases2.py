'''
crear una clase con tres notas
crear un bucle que crea de 1 a 5 alumnos y mete notas del 1 al 10
metodo para decir si la nota 1, 2 y 3 esta suspensa
nota media de todos los alumnos
'''
from random import randint

class Alumno:
	def __init__(self, nota1, nota2, nota3):
		self.nota1 = nota1
		self.nota2 = nota2
		self.nota3 = nota3

	def suspensas(self):
		notas = self.notas()
		cont = 1
		for nota in notas:
			if nota >= 5:
				print('La nota', cont, 'esta aprobada')
			else:
				print('La nota', cont, 'esta suspensa')

			cont += 1

	def notas(self):
		return [self.nota1, self.nota2, self.nota3]

	def __str__(self):
		return str(self.nota1) + ' ' + str(self.nota2) + ' ' + str(self.nota3)

lista = []
for i in range(randint(1, 5)):
	alumno1 = Alumno(randint(1, 10), randint(1, 10), randint(1, 10))
	lista.append(alumno1)
	print(alumno1)
	alumno1.suspensas()

total = 0
for alumno in lista:
	total += sum(alumno.notas()) / len(alumno.notas())

print('La media es', total/len(lista))