tam = int(input('Número de votos: '))

votos = []
for i in range(tam):
    cadena = str(tam-i) + ' restantes. Voto: '
    votos.append(int(input(cadena)))
    
votos_blanco = votos.count(0)
votos_1 = votos.count(1)
votos_2 = votos.count(2)
votos_3 = votos.count(3)
votos_nulos = len(votos) - votos_blanco - votos_1 - votos_2 - votos_3

print('Votos en blanco:', votos_blanco)
print('Votos del candidato 1:', votos_1)
print('Votos del candidato 2:', votos_2)
print('Votos del candidato 3:', votos_3)
print('Votos nulos:', votos_nulos)