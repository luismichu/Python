import json

with open("archivo.json", "r") as fic:
	cadena = json.load(fic)

print(cadena)

diccionario = json.loads(cadena)
print(diccionario)
print(diccionario['Fruteria'][0]['Fruta'][0]['Nombre'], diccionario['Fruteria'][0]['Fruta'][0]['Cantidad'])