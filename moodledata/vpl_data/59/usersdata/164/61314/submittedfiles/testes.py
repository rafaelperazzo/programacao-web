# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def valorabsoluto(x):
    if (x<0):
        x=x*(-1)
    else:
        x=x*1
    return(x)    
    
def pi(m):
    cont=0
    soma=3
    a=0
    b=2
    for i in range (1, m+1, 1):
        a=4/(b*(b+1)*(b+2))
        cont=cont+1
        if (cont%2==1):
            soma=soma+a
        if (cont%2==0):
            soma=soma-a    
        b=b+2
    return(soma)

def fat(d):
    f=1
    while (d>0):
        f=f*d
        d=d-1
    return(f)
    
def cos(x, epsilon):
    cont=0
    soma=1
    c=0
    d=2
    c=(x**d)/fat(d)
    while (c>epsilon):    
        cont=cont+1
        if (cont%2==1):
            soma=soma-c
        if (cont%2==0):
            soma=soma+c
        d=d+2
        c=(x**d)/fat(d)    
    return(soma)
    
def razaoaurea(m, epsilon):
    x=pi(m)/5
    g=cos((e),(epsilon))
    razao=2*e
    return(razao)


m=int(input('Digite o número de termos para PI: '))
epsilon=float(input('Digite o epsilon para o cálculo da razão aurea: '))
print('%.15f' %pi(m))
print('%.15f' %cos(x, epsilon))
print('%.15f' %razaoaurea(m, epsilon))