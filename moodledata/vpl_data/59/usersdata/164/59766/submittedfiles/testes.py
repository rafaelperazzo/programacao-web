# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import math
npi=int(input('Digite o número de termos para PI: '))
contpi=0
somapi=3
a=0
b=2
contcos=0
somacos=1
c=0
d=2
k=1
e=d

for i in range (1, npi+1, 1):
    a=4/(b*(b+1)*(b+2))
    contpi=contpi+1
    if (contpi%2==1):
        somapi=somapi+a
    if (contpi%2==0):
        somapi=somapi-a    
    b=b+2
    x=somapi
    c=(x**d)/(math.factorial(d))
    contcos=contcos+1
    if (contcos%2==1):
        somacos=somacos-c
    if (contcos%2==0):
        somacos=somacos+c
    d=d+2
razao=2*c    
print('%.15f' %somapi)
print('%.15f' %somacos)
