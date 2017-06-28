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
    return(x)

def fat(d):
    z=1
    while (d>0):
        z=z*d
        d=d-1
    return(z)



npi=int(input('Digite o número de termos para PI: '))
epsilon=float(input('Digite o epsilon para o cálculo da razão aurea: '))
print('%.15f' %pi(x))
print('%.15f' %razao)