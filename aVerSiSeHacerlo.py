d = {'11': [0.76700000000000002, 3455.0, 0.76700000000000002, 0.76700000000000002, 34.0, 0.76700000000000002], 
'22': [34.0, 0.76700000000000002]}

d2 = {lista0 : round(sum(lista1), 2) for lista0, lista1 in d.items()}
print(d2)

d3 = {num : pow(num, 2) for num in range(2, 9) if num%2 == 0}
print(d3)