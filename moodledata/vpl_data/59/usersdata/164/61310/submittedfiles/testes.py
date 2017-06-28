# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def valorabsoluto(x):
    if (x<0):
        x=x*(-1)
    else:
        x=x*1
    return(x)    
    
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

def fat(d):
    f=1
    while (d>0):
        f=f*d
        d=d-1
    return(f)
    
def cos(x, epsilon):
    contcos=0
    somacos=1
    c=0
    d=2
    c=(x**d)/fat(d)
    while (c>epsilon):    
        contcos=contcos+1
        if (contcos%2==1):
            somacos=somacos-c
        if (contcos%2==0):
            somacos=somacos+c
        c=(x**d)/fat(d)    
        d=d+2
    return(somacos)
    
def razaoaurea(m, epsilon):
    e=cos((pi(m)/5)(epsilon))
    razao=2*e
    return(razao)


m=int(input('Digite o número de termos para PI: '))
epsilon=float(input('Digite o epsilon para o cálculo da razão aurea: '))
x=0
print('%.15f' %pi(m))
print('%.15f' %cos(x, epsilon))
print('%.15f' %razaoaurea(m, epsilon))