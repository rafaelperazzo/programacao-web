# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
npi=int(input('Digite o número de termos para PI: '))
nep=float(input('Digite o número de termos para Epsilon: '))
contpi=0
somapi=3
a=0
b=2

contep=0
somaep=1
c=0
d=2
x=a/5
k=1

for i in range (1, npi+1, 1):
    a=4/(b*(b+1)*(b+2))
    contpi=contpi+1
    if (contpi%2==1):
        somapi=somapi+a
    if (contpi%2==0):
        somapi=somapi-a    
    b=b+2
    while (d>0):
        k=k*d
        d=d-1
        c=(x**d)/(fat(d*2))
        contep=contep+1
        if (contep%2==1):
            somaep=somaep-c
        if (contep%2==0):
            somaep=somaep+a    
        d=d+2
print('%.15f' %somapi)


razao=2*c
print('%.15f' %razao)

