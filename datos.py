datos = {'nombre':[], 'telefono':[], 'edad':[], 'fecha_nac':[]}

nombre = input('Nombre: ')

while nombre != '':
	telefono = input('Telefono: ')
	edad = input('Edad: ')
	fecha_nac = input('Fecha de nacimiento: ')

	datos.update({'nombre':datos.get('nombre') + [nombre]})
	datos.update({'telefono':datos.get('telefono') + [telefono]})
	datos.update({'edad':datos.get('edad') + [edad]})
	datos.update({'fecha_nac':datos.get('fecha_nac') + [fecha_nac]})
	
	nombre = input('Nombre: ')
	

print('')
for i in range(len(datos.get('nombre'))):
	print('Nombre:', datos.get('nombre')[i])
	print('Telefono:', datos.get('telefono')[i])
	print('Edad:', datos.get('edad')[i])
	print('Fecha de nacimiento:', datos.get('fecha_nac')[i], '\n')
	