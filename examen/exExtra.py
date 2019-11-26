codigo = 7702004003508


lista_codigo = []
while codigo != 0:
    lista_codigo.append(codigo%10)
    codigo //= 10
    
lista_codigo.reverse()

if len(lista_codigo) == 13:
    resultado = 0
    for i in range(0, len(lista_codigo)-1):
        if (i+1)%2 == 0:
            resultado += lista_codigo[i] * 3
        else:
            resultado += lista_codigo[i]
       
    resultado = ((resultado//10) + 1) * 10 - resultado

    if resultado == lista_codigo[-1]:
        print('Coincide con el código de control. El código es correcto')
    else:
        print('No coincide. El código es incorrecto')
else:
    print('El código no tiene 13 dígitos')