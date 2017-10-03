n = int(input('Digite o número de lados do polígono: '))

if n>2:
    nd = (n*(n-3))/2
    print('seu polígono tem: ',nd,'diagonais diferentes')
    
else:
    print('isso não é um polígono')
    