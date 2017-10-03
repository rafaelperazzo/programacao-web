#Programa para descobrir quantas diagonais diferentes têm em um polígono de 'n' lados.

n = int(input('Digite o número de lados do polígono: '))
if n>2:
    nd = (n*(n-3))/2
    print('Seu polígono tem',nd,'diagonais diferentes')
    
else:
    print('Isso não é um polígono')
    