while True:
    lista = [int(input('Número: ')) for i in range(3)]
    
    if all([True if elem>=5 and elem<=10 else False for elem in lista]):
        print('OK')
        break
    else:
        if any([True if elem>=5 and elem<=10 else False for elem in lista]):
            print('Hay al menos uno mal. Repite')
        else:
            print('Todos mal. Ni lo intentes')
            break