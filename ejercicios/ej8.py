lista = ['123 Juan 26', '234 María 25', '345 José 22']

dic = dict()
for elemento in lista:
    idNum = int(elemento[:elemento.index(' ')]) #subcadena desde el principio hasta el primer espacio
    nombre = elemento[elemento.index(' ') + 1:elemento.rindex(' ')] # desde el primer espacio hasta el ultimo
    edad = int(elemento[elemento.rindex(' '):]) # desde el ultimo espacio hasta el final
    dic.update({idNum:(nombre, edad)})
    
print(dic)

