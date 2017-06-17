# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
npi=int(input('Digite o número de termos para PI: '))
nep=int(input('Digite o número de termos para Epsilon: '))
contpi=0
somapi=3
a=0
b=2
for i in range (0, npi, 1):
    a=4/(b*(b+1)*(b+2))
    contpi=contpi+1
    if (contpi%2==0):
        somapi=somapi-a    
    if (contpi%2==1):
        somapi=somapi+a
    b=b+2
print('%.15f' %somapi)



