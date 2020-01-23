'''
crear una clase llamada alumno con los atributos con un metodo inicializar: nombre, edad, 
peso y asignatura favorita
crear un alumno
metodo para imprimir el nombre es x, la edad es x...

llamar a metodo devolver_masa_iq(): return edad * peso / 3
imprimir el objeto y que devuelva una lista
'''

class Alumno:
	def inicializar(self, nombre, edad, peso, asignatura_favorita):
		self.nombre = nombre
		self.edad = edad
		self.peso = peso
		self.asignatura_favorita = asignatura_favorita

	def imprimir(self):
		print('El nombre es', self.nombre)
		print('La edad es', self.edad, 'años')
		print('El peso es', self.peso, 'kilos')
		print('La asignatura favorita es', self.asignatura_favorita)

	def devolver_masa_iq(self):
		return self.edad * self.peso / 3

	def __str__(self):
		return self.nombre + ' ' + str(self.edad) + ' ' + str(self.peso) + ' ' + self.asignatura_favorita


alumno1 = Alumno()
alumno1.inicializar('Juan', 18, 62, 'Mates')

alumno1.imprimir()

print('La masa iq del alumno es',alumno1.devolver_masa_iq())
print(alumno1)
print(list(str(alumno1).split(' ')))