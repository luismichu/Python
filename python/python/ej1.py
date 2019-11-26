def alquilar_o_comprar():
	codigo = int(input('Codigo de pelicula: '))
	print('1. Alquiler')
	print('2.Compra')
	alquiler = int(input('Elige opcion: '))

	cuenta = 0
	if alquiler == 1:
		dias = int(input('Cuantos dias quieres alquilar?: '))
		dia = 4
		for dia in range(dia, dia+dias):
			cuenta += blockbuster['precio alquiler'][codigo-1]
			if dia%7 == 5 or dia%7 == 6:
				cuenta += blockbuster['precio alquiler'][codigo-1]*0.15
			dia += 1

	elif alquiler == 2:
		cuenta += blockbuster['precio'][codigo-1]
		
		print('1. Seguir comprando')
		print('2. Salir')
		seguirComprando = int(input('Elige opcion: '))
		while seguirComprando == 1:
			codigo = int(input('Codigo de pelicula: '))
			cuenta += blockbuster['precio'][codigo-1]

			print('1. Seguir comprando')
			print('2. Salir')
			seguirComprando = int(input('Elige opcion: '))

	print('Cuenta: ', cuenta)


def ver_categoria_infantil():
	pos = []
	categorias = blockbuster['categoria']
	for i in range(len(blockbuster['categoria'])):
		if blockbuster['categoria'][i] == 'Infantil':
			pos.append(i)

	print('Infantil:')
	precio = 0
	for num in pos:
		print(blockbuster['Pelicula'][num], str(blockbuster['precio'][num])+'€')
		precio += blockbuster['precio'][num]

	print('Precio total:', str(precio)+'€')


def nueva_pelicula():
	print('\nNueva pelicula')
	blockbuster['Pelicula'].append(input('Titulo: '))
	blockbuster['categoria'].append(input('Categoria: '))
	blockbuster['codigo'].append(input('Codigo: '))
	while(True):
		try:
			blockbuster['precio'].append(float(input('Precio: ')))
		except:
			print('Tipo de dato incorrecto')
		else:
			break
	while True:
		try:
			blockbuster['precio alquiler'].append(float(input('Precio alquiler: ')))
		except:
			print('Tipo de dato incorrecto')
		else:
			break

	imprimir()


def cambiar_pokemon_por_digimon():
	blockbuster['Pelicula'][0] = 'Digimon'
	print([precio for precio in blockbuster['precio']])
	blockbuster['precio'] = [precio+precio*0.48 for precio in blockbuster['precio']]
	imprimir()


def	imprimir():
	for key,item in blockbuster.items():
		print(key, item)

	print()


blockbuster = {'Pelicula':['Pokemon', 'Los vengadores', 'Toy Story', 'IT'], 'categoria':['Infantil', 'Accion', 'Infantil', 'Terror'], 'codigo':[1,2,3,4], 'precio':[10.0, 20.5, 15.3, 22.3], 'precio alquiler':[2, 3.2, 1.5, 1.7]}
imprimir()

opciones = {1:'Alquilar o comprar', 2:'Ver categoria infantil', 3:'Nueva pelicula', 4:'Cambiar Pokemon por Digimon', 5:'Salir'}
funciones = {1:alquilar_o_comprar, 2:ver_categoria_infantil, 3:nueva_pelicula, 4:cambiar_pokemon_por_digimon}
for num, opcion in opciones.items():
	print(str(num) + ':', opcion)

while(True):
	try:
		eleccion = int(input('Elige opcion: '))
	except:
		print('Tipo de dato incorrecto')
	else:
		break

print()
if eleccion in funciones.keys():
	funciones[eleccion]()