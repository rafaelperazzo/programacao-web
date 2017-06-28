# -*- coding: utf-8 -*-
def degrau (v,l):
    for i in range (0,n-1,1):
        l.append(l[i]-v[i+1])
    for i in range (0,len(l),1):
        if (l[i]<0):
        l[i]<l[i]*(-1)
    return (l)
n=int(input('escreva a quantidade de elementos:'))
v=[]
l=[]
for i in range (0,n,1):
    valor=int(input('valor da lista:'))
    v.append(valor)
print(degrau(v,l))