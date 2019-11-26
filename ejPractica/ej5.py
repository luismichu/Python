def main():
    n = int(input('Número de términos: '))
    
    print('Pi con precisión de', n, ':', pi(n))
    
    
def pi(n):
    resultado = 1
    flag = True
    n = n*2 +3
    for i in range(3, n, 2):
        if flag:
            resultado = resultado - (1/i)
            flag = False
        else:
            resultado = resultado + (1/i)
            flag = True
        
    return resultado * 4
    
    
    
    
if __name__ == '__main__':
    main()

