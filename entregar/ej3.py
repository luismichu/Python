Fruta_fresca = ['    banana', 'mora de Logan    ', ' maracuya   ']

fruta_sin_espacios = [''.join([letra for letra in fruta if letra != ' ']) for fruta in Fruta_fresca]

print(Fruta_fresca)
print(fruta_sin_espacios)