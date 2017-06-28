# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def pi(m):
    contpi=0
    somapi=3
    a=0
    b=2
    for i in range (1, m+1, 1):
        a=4/(b*(b+1)*(b+2))
        contpi=contpi+1
        if (contpi%2==1):
            somapi=somapi+a
        if (contpi%2==0):
            somapi=somapi-a    
        b=b+2
    return(somapi)
    
def valorabsoluto(x):
    x=somapi/5
    return(x)

def fat(d):
    z=1
    while (d>0):
        z=z*d
        d=d-1
    return(z)



m=int(input('Digite o número de termos para PI: '))
epsilon=float(input('Digite o epsilon para o cálculo da razão aurea: '))
x=0
print('%.15f' %pi(m))
print('%.5f' %valorabsoluto(x))
print('%.15f' %razao)