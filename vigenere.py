def cifrar(cadena):
	cad_cifrada = [str((ord(cadena[i])+3)%100) for i in range(len(cadena))]
	cad_cifrada = ''.join(cad_cifrada)
	return int(cad_cifrada)*int(cad_cifrada)

print(cifrar('holaz'))
