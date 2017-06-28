# -*- coding: utf-8 -*-
def degrau(x):
    for i in range(0,len(x),1):
        d=[]
        c=x[i]-x[i+1]
        d.append(c)
    return(d)


n=int(input('digite quantos elementos na lista você quer:'))
a=[]
for i in range(0,n,1):
    lista=int(input('digite o elemento da lista:'))
    a.append(lista)

print(degrau(a))
