# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
npi=int(input('Digite o número de termos para PI: '))
epsilon=float(input('Digite o epsilon para o cálculo da razão aurea: '))
contpi=0
somapi=3
a=0
b=2
contcos=0
somacos=1
c=0
d=2

def fat(d):
    while (d>0):
        z=1
        z=z*d
        d=d-1
    return(fat)

for i in range (1, npi+1, 1):
    a=4/(b*(b+1)*(b+2))
    contpi=contpi+1
    if (contpi%2==1):
        somapi=somapi+a
    if (contpi%2==0):
        somapi=somapi-a    
    b=b+2
    x=somapi
        
while(somacos>epsilon):
    cos=(x**d)/(fat)
    if (contcos%2==1):
        somacos=somacos-d
    if (contcos%2==0):
        somacos=somacos+d    
    d=d+2

print('%.15f' %somapi)
print('%.15f' %somacos)