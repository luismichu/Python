from functools import reduce

def ejercicio1():
	poema = 'Porque te tengo y no\n'\
			'porque te pienso\n'\
			'porque la noche está de ojos abiertos\n'\
			'porque la noche pasa y digo amor\n'\
			'porque has venido a recoger tu imagen\n'\
			'y eres mejor que todas tus imágenes\n'\
			'porque eres linda desde el pie hasta el alma\n'\
			'porque eres buena desde el alma a mí\n'\
			'porque te escondes dulce en el orgullo\n'\
			'pequeña y dulce\n'\
			'corazón coraza\n'\
			'porque eres mía\n'\
			'porque no eres mía\n'\
			'porque te miro y muero\n'\
			'y peor que muero\n'\
			'si no te miro amor\n'\
			'si no te miro\n'\
			'porque tú siempre existes dondequiera\n'\
			'pero existes mejor donde te quiero\n'\
			'porque tu boca es sangre\n'\
			'y tienes frío\n'\
			'tengo que amarte amor\n'\
			'tengo que amarte\n'\
			'aunque esta herida duela como dos\n'\
			'aunque te busque y no te encuentre\n'\
			'y aunque\n'\
			'la noche pase y yo te tenga\n'\
			'y no.\n'\

	with open('poema.txt', 'w') as file:
		file.write(poema)

	with open('poema.txt', 'r') as file:
		fic = [line for line in file]
		longitud = len(fic)
		print('Lineas del poema:', longitud)
		palabras, espacios, carac = 0, 0, 0
		for line in fic:
			palabras += len(line.split())
			espacios += line.count(' ')
			carac += len(line[:-1])

		print('Palabras:', palabras)
		print('Espacios:', espacios)
		print('Caracteres:', carac)

		return longitud, palabras, espacios, carac


def ejercicio2():
	longitud, palabras, espacios, carac = ejercicio1()

	with open('poema.txt', 'a') as file:
		file.write('\nLineas del poema: ' + str(longitud) + '\n')
		file.write('Palabras: ' + str(palabras) + '\n')
		file.write('Espacios: ' + str(espacios) + '\n')
		file.write('Caracteres: ' + str(carac) + '\n')

def ejercicio3(lista):
	print(list(map(lambda x: x*-1, lista)))
	print(reduce(lambda x, y: x if y <= 0 else x+y, lista))
	print(list(filter(lambda x: x >= 0, lista)))


def ejercicio4(lista):
	print(reduce(lambda x, y: x*y, lista))

#ejercicio1() #el ejercicio2 llama a esta funcion
ejercicio2()
ejercicio3([1, -3, -45, 32, 73, -50, -37, 2])
ejercicio4([1, 2, 3, 4, 'palabra '])