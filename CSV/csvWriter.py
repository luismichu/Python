import csv

paises = ['españita', 'españita2', 'gibraltarEspañol']
ciudades = ['ciudad1', 'ciudad2', '12345']
ciudades2 = ['ciudad4', 'ciudad5', 'ciudad6']
ciudades3 = ['54321', 'ciudad8', 'ciudad9']

lista_ciudades = [ciudades, ciudades2, ciudades3]

with open('archivo.csv', 'w') as fic:
	writer = csv.DictWriter(fic, fieldnames=paises, delimiter='?')
	writer.writeheader()

	for ciudades in lista_ciudades:
		writer.writerow(dict(zip(paises, ciudades)))