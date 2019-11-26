dia = int(input('Introduce el dia de nacimiento: '))
mes = int(input('Introduce el mes de nacimiento: '))
anio = int(input('Introduce el año de nacimiento: '))

resultado = dia + mes + anio
num_magico = 0
while resultado != 0:
    num_magico += resultado % 10
    resultado //= 10
        
while num_magico >= 10:
    resultado = num_magico
    num_magico = 0
    while resultado != 0:
        num_magico += resultado % 10
        resultado //= 10
    
print('Tu número mágico es:', num_magico)
print('Tu fecha de nacimiento es:')
print('{:0>2}'.format(str(dia)), '{:0>2}'.format(str(mes)), anio, sep='/')


