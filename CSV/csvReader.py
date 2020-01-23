import csv

with open('archivo.csv', 'r') as fic:
	fic = csv.DictReader(fic, delimiter='?')
	fic.getheader()
	cont = 0
	dic = dict()
	for row in fic:
		if cont == 0:
			for key in dict(row).keys():
				dic.update({key : []})
			cont += 1

		for key, value in dict(row).items():
			dic[key] = dic[key] + [value]

print(dic)
for key, value in dic.items():
	for ciudad in value:
		if len(ciudad) < 7:
			print('La ciudad', ciudad, 'del pais', key, 'tiene menos de 7 caracteres')