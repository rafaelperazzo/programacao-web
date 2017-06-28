# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def pi(x):
    contpi=0
    somapi=3
    x=0
    a=2
    for i in range (1, npi+1, 1):
        x=4/(a*(a+1)*(a+2))
        contpi=contpi+1
        if (contpi%2==1):
            somapi=somapi+x
        if (contpi%2==0):
            somapi=somapi-x    
        a=a+2

def fat(d):
    z=1
    while (d>0):
        z=z*d
        d=d-1
    return(z)



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
    c=(x**d)/(fat(d))
    contcos=contcos+1
    if (contcos%2==1):
        somacos=somacos-c
    if (contcos%2==0):
        somacos=somacos+c    
    d=d+2
    
razao=2*somacos    

print('%.15f' %somapi)
print('%.15f' %razao)
