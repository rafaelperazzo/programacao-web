# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
npi=int(input('Digite o número de termos para PI: '))
nep=float(input('Digite o número de termos para Epsilon: '))
contpi=0
somapi=3
a=0
b=2
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
    while (d>0):
        k=k*e
        e=e-1
        c=(x**d)/(e)
        if (contcos%2==1):
            somacos=somacos-c
        if (contcos%2==0):
            somacos=somacos+c
    razao=2*c    
print('%.15f' %somapi)
print('%.15f' %razao)
