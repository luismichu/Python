from random import randint as aleatorio, choice as eleccion, shuffle as desordenar

def genera_jugador():
	vida = float(aleatorio(50, 100))
	ataque = float(aleatorio(40, 60))
	defensa = float(aleatorio(20, 40))
	habilidad = eleccion(['fuego', 'agua', 'planta'])

	return {'vida':vida, 'ataque':ataque, 'defensa':defensa, 'habilidad':habilidad}


def genera_enemigo(jugador):
	enemigo = dict()
	
	enemigo['vida'] = round(jugador['vida'] * 0.6, 2)
	enemigo['ataque'] = float(aleatorio(40, 55))
	enemigo['defensa'] = float(aleatorio(15, 35)) 
	enemigo['habilidad'] = eleccion(['fuego', 'agua', 'planta'])

	return enemigo


def comprobar_ventaja(jugador, enemigo):
	ventaja = (jugador['habilidad'], enemigo['habilidad'])
	ventajas = [('fuego', 'planta'), ('planta', 'agua'), ('agua', 'fuego')]
	return True if ventaja in ventajas else False


def imprimir_estadisticas(diccionario):
	for clave, valor in diccionario.items():
		print(' -' + '{:9s}'.format(clave) + ':', str('*'*int((valor//5)) + ', ' + str(valor)) if type(valor) == float else valor)


def trampa(jugador):
	print('\n##Trampa##')

	estadistica = eleccion(['vida', 'ataque', 'defensa'])
	print('Te ha bajado', estadistica)
	if estadistica == 'ataque' or estadistica == 'defensa':
		jugador[estadistica] = round(jugador[estadistica] * 0.9, 2)
	elif estadistica == 'vida':
		jugador[estadistica] = round(jugador[estadistica] * 0.8, 2)

	imprimir_estadisticas(jugador)


def combate(jugador):
	print('\n##Combate##')
	enemigo = genera_enemigo(jugador)
	print('>Tus estadisticas:')
	imprimir_estadisticas(jugador)
	print('>Estadisticas del enemigo:')
	imprimir_estadisticas(enemigo)
	while jugador['vida'] > 0:
		ataque = jugador['ataque']
		if comprobar_ventaja(jugador, enemigo):
			ventaja = 'con ventaja'
			ataque += ataque * 0.1
		else:
			ventaja = ''

		print('\nAtacas', ventaja)

		ataque -= enemigo['defensa']
		enemigo['vida'] = round(enemigo['vida'] - ataque, 2)
		
		if enemigo['vida'] <= 0:
			print('Vida del enemigo: 0')
			print('Victoria!!')
			break
		else:
			print('Vida del enemigo:', str('*'*int((enemigo['vida']//5))), enemigo['vida'])
			input('Intro para continuar...')
			ataque = enemigo['ataque']
			if comprobar_ventaja(enemigo, jugador):
				ventaja = 'con ventaja'
				ataque += ataque * 0.1
			else:
				ventaja = ''

			print('\nAtaca el enemigo', ventaja)
			ataque -= jugador['defensa']
			jugador['vida'] = round(jugador['vida'] - ataque, 2)
			
			print('Tu vida:', str('*'*int((jugador['vida']//5))), jugador['vida'])
			input('Intro para continuar...')

	if jugador['vida'] <= 0:
		print('Has muerto')
	else:
		imprimir_estadisticas(jugador)



def adivinar_numero(jugador):
	print('\n##Adivina el numero de 1 a 10##')
	num = aleatorio(1, 10)
	adiv = int(input('Adivina el numero: '))
	while adiv != num:
		jugador['vida'] = round(jugador['vida'] - 5, 2)
		if jugador['vida'] <= 0:
			break
		print('Tu vida:', str('*'*int((jugador['vida']//5))), jugador['vida'])
		adiv = int(input('Adivina el numero: '))

	if num == adiv:
		print('Enhorabuena!! Has adivinado el numero')
		imprimir_estadisticas(jugador)
	else:
		print('Has muerto. Num:', num)



def main():
	nombre = input('Nombre del jugador: ')
	print('Saludos,', nombre)
	print('Tus estadisticas:')
	jugador = genera_jugador()
	imprimir_estadisticas(jugador)
	for i in range(1, 3):
		input('Intro para continuar...')
		combate(jugador)
		puertas = [trampa, combate, adivinar_numero]
		desordenar(puertas)
		print('\n///Prueba', i,  '\\\\\\')
		puerta = int(input('Elige una puerta. Numero del 1 al 3: '))
		puertas[puerta-1](jugador)

		if jugador['vida'] <= 0:
			break

	if jugador['vida'] > 0:
		print('\nHas conseguido sobrevivir')
	else:
		print('\nPues vaya un heroe...')
	
	


if __name__ == '__main__':
	main()