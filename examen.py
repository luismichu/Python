#crear lista e introducir palabras hast que quiera el usuairo, controlar  excepciones,
#a tarves de una funcion contar las vocales
l = []

resp=''

while resp!='n':
	boolean=False
	while not boolean:
		try:
			pal = input("Elige una palabra: ")
			l.append(pal)
			resp= input("¿Desea continuar? (s/n) ")
			resp=resp.lower()
			while resp!='n' and resp!='s':
				resp= input("Introduzca s o n: ")
				resp=resp.lower()
			boolean = True
		except Excepcion:
			print('Excepcion')

print(l)
voc=0
vocales = ['a', 'e', 'i', 'o', 'u']
for i in l:
	for j in i:
		if j in vocales:
			voc+=1

print(voc)
