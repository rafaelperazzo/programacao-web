# -*- coding: utf-8 -*-
def degrau(x):
    for i in range(0,len(x),1):
        c=x[i]-x[i+1]
    return(c)


n=int(input('digite quantos elementos na lista você quer:'))
a=[]
for i in range(0,n,1):
    lista=int(input('digite o elemento da lista:'))
    a.append(lista)

print(degrau(a))
