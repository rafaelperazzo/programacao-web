# -*- coding: utf-8 -*-

def degrau(z):
    k=0
    degrau=0
    for i in range(0,len(b)-1,1):
        k=z[i]-z[i+1]
        if k<0:
            k=k*(-1)
        if k>degrau:
            degrau=k
    return(degrau)
n=int(input('digite a quantidade de elementos:'))
x=[]
for i in range(0,n,1):
    valor=int(input('digite o elemento:'))
    x.append(valor)
print(degrau(x))

