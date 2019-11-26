dic = {'GSP1271': ['Chevrolet', 25000, 18500.0], 'GRT2438': ['Ford', 15000, 1780.0]}
separador = ';'
cadena = ""

for elem in dic.items():
    cadena += elem[0] #se concatena la clave
    for sub_elem in elem[1]:
        cadena += ' ' + str(sub_elem) #se concatena cada elemento de la lista
    cadena += separador #se concatena el separador
    
print(cadena)