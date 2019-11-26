def main():
    a = int(input('Número 1: '))
    b = int(input('Número 2: '))
    
    a = divisores(a)
    b = divisores(b)
    resultado = 1
    
    for elem in a:
        if elem in b:
            b.remove(elem)
            resultado *= elem
            
    print('M.C.D.:', resultado)
    
def divisores(num):
    div = []
    while num > 1:
        i = 2
        while i < num and num%i != 0:
            i += 1
        
        num /= i
        div.append(i)
        
    return div
            
if __name__ == '__main__':
    main()
            
