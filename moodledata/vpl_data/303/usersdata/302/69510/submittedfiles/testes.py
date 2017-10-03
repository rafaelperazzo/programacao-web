n = float(input('Digite o número de lados do polígono'))

if n>2:
    
    nd = ((n*(n-3))/2)

print (nd)
else:
    print('Isso não é um polígono')
