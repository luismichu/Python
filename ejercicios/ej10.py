S='GSP1271 Chevrolet 25000 18500.00;GRT2438 Ford 15000 17800;'
separador = ';'

cad = S
dic = dict()
while cad.find(separador) != -1:
    aux = cad[:cad.find(separador)] #subcadena hasta el primer separador
    placa = aux[:aux.find(' ')] #hasta el primer espacio
    aux = aux[aux.find(' ') + 1:] #se borra el espacio
    marca = aux[:aux.find(' ')] #se repite 4 veces
    aux = aux[aux.find(' ') + 1:]
    km = int(aux[:aux.find(' ')])
    aux = aux[aux.find(' ') + 1:]
    precio = float(aux)
    
    dic.update({placa:[marca, km, precio]})    
    cad = cad[cad.find(separador) + 1:] #se borra el separador
    
print(dic)