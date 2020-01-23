'''
clase principal vehiculo con marca y modelo
metodo que dice si la marca del coche empieza por vocal esta guay y si no esta feo

clase moto que hereda de vehiculo
parametro etiqueta medioambiental y año
metodo que dice si cumple normativa
mostrar

clase lancha que hereda de vehiculo
parametro nudos maximos
metodo que dice marca, modelo y nudos max
'''

class Vehiculo():
	def __init__(self, marca, modelo):	
		self.marca = marca
		self.modelo = modelo

	def empieza_por_vocal(self):
		if self.marca[0].lower() in 'aeiou':
			print('El coche esta guay')
		else:
			print('ta feo')

class Moto(Vehiculo):
	def __init__(self, marca, modelo, etiqueta, anyo):
		super().__init__(marca, modelo)
		self.etiqueta = etiqueta
		self.anyo = anyo

	def cumple_normativa(self):
		return True if self.anyo < 2000 and self.etiqueta < 'E' else False
		
	def __str__(self):
		return self.marca + ' ' + self.modelo + ', anyo ' + str(self.anyo) + ' y etiqueta ' + self.etiqueta

class Lancha(Vehiculo):
	def __init__(self, marca, modelo, nudos):
		super().__init__(marca, modelo)
		self.nudos = nudos

	def mostrar(self):
		print('Marca:', self.marca)
		print('Modelo:', self.modelo)
		print('Nudos maximos:', self.nudos)


v1 = Vehiculo('Ford', 'Mustang')
v2 = Vehiculo('Aston Martin', 'DB9')

print('Vehiculo 1')
v1.empieza_por_vocal()

print('Vehiculo 2')
v2.empieza_por_vocal()
		
m1 = Moto('Yamaha', 'YZF-R6', 'B', 2019)
m2 = Moto('Honda', 'CBR1000RR', 'E', 1998)

if m1.cumple_normativa():
	print('\nLa moto 1 cumple la normativa')
else:
	print('\nLa moto 1 no cumple la normativa')

if m2.cumple_normativa():
	print('La moto 2 cumple la normativa')
else:
	print('La moto 2 no cumple la normativa')

print('')
print(m1)
print(m2)

l1 = Lancha('Marca1', 'Modelo1', 12)
l2 = Lancha('Marca2', 'Modelo2', 14)

print('\nDatos de la lancha 1')
l1.mostrar()
print('\nDatos de la lancha 2')
l2.mostrar()