# -*- coding: utf-8 -*-
def degrau(x):
    d=[]
    for i in range(0,len(x),1):
        c=x[i]-x[i+1]
        if c<0:
            c=c*(-1)
        d.append(x)
    return(d)


n=int(input('digite quantos elementos na lista você quer:'))
a=[]
for i in range(0,n,1):
    lista=int(input('digite o elemento da lista:'))
    a.append(lista)

print(degrau(a))
