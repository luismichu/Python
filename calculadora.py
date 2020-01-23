'''
clase Calculadora
init
datos por pantalla en el constructor
'''

class Calculadora:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def suma(self):
		return self.num1 + self.num2

	def resta(self):
		return self.num1 - self.num2

	def mult(self):
		return self.num1 * self.num2

	def div(self):
		return self.num1 / self.num2


calc = Calculadora(int(input('Primer numero: ')), int(input('Segundo numero: ')))

print('Suma:', calc.suma())
print('Resta:', calc.resta())
print('Multiplicacion:', calc.mult())
print('Division:', calc.div())