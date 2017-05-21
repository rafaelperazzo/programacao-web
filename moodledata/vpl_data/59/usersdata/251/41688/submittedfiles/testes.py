# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input('Digite a quantidade de termos: '))
somatorio=0
for termo in range(1,n+1,1):
    m = float(input('Digite o valor do termo %d'+%termo+''))
    m2 = m**2
    somatorio = somatorio+m2
    
var = (somatorio/n)

print('%.5f'%var)
