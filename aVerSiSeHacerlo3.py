cad = '0000000000000000es un ejemplo de string con ceros¡!! 00000000'
cad = input('cadena: ')
if cad.isalpha():
	print(cad)
elif cad.isalnum():
	print(cad.strip('0').strip())
else:
	print('Cadena no valida')

frutas = ['banana', 'mora de Logan ', 'maracuyá ']
print([fruta.strip() for fruta in frutas])

cad2 = 'a: b: c: d: e: f'
print(','.join(cad2.split(':')))