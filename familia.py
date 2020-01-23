'''
abuelo
-riqueza
-tierras

hijo1
-enfermedad
-color ojos

hijo2
-altura
-color pelo

nieto1
-estado civil
-nombre

nieto2
-hijos
-nombre
'''

class Abuelo():
	def __init__(self, riqueza, tierras):
		self.riqueza = riqueza
		self.tierras = tierras

class Hijo1(Abuelo):
	def __init__(self, riqueza, tierras, enfermedad, color_ojos):
		super().__init__(riqueza, tierras)
		self.enfermedad = enfermedad
		self.color_ojos = color_ojos

class Hijo2(Abuelo):
	def __init__(self, riqueza, tierras, altura, color_pelo):
		super().__init__(riqueza, tierras)
		self.altura = altura
		self.color_pelo = color_pelo

class Nieto1(Hijo1):
	def __init__(self, riqueza, tierras, enfermedad, color_ojos, estado_civil, nombre):
		super().__init__(riqueza, tierras, enfermedad, color_ojos)
		self.estado_civil = estado_civil
		self.nombre = nombre

class Nieto2(Hijo2):
	def __init__(self, riqueza, tierras, altura, color_pelo, hijos, nombre):
		super().__init__(riqueza, tierras, altura, color_pelo)
		self.hijos = hijos
		self.nombre = nombre

class Nieto3(Hijo1, Hijo2):
	def __init__(self, riqueza, tierras, enfermedad, color_ojos, altura, color_pelo, lugar_muerte, fecha_muerte):
		super().__init__(riqueza, tierras, enfermedad, color_ojos)
		super().__init__(riqueza, tierras, altura, color_pelo)
		self.lugar_muerte = lugar_muerte
		self.fecha_muerte = fecha_muerte

n = Nieto2(2000, 'Españita', 1.75, 'castaño', 5, 'Francisco')

print('El nieto', n.nombre, 'tiene', n.hijos, 'hijos, el pelo', n.color_pelo, ', mide', n.altura, 'm, su tierra es', n.tierras, 'y su riqueza', n.riqueza)

n3 = Nieto3(2000, 'Españita', 'SIDA', 'azul', 1.6, 'rubio', 'Mostoles', '20/01/2020')