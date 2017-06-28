# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def pi(npi):
    contpi=0
    somapi=3
    m=0
    a=2
    for i in range (1, npi+1, 1):
        m=4/(a*(a+1)*(a+2))
        contpi=contpi+1
        if (contpi%2==1):
            somapi=somapi+m
        if (contpi%2==0):
            somapi=somapi-m    
        a=a+2
    return(somapi)

def fat(d):
    z=1
    while (d>0):
        z=z*d
        d=d-1
    return(z)



npi=int(input('Digite o número de termos para PI: '))
epsilon=float(input('Digite o epsilon para o cálculo da razão aurea: '))
print('%.15f' %pi(npi))
print('%.15f' %razao)