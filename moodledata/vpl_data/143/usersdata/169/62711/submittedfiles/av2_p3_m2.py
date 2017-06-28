# -*- coding: utf-8 -*-
n=int(input('Digite a Quantidades de Termos da Lista:'))
l1=[]
for i in range(0,n,1):
    n=int(input('Digite os Valores da Lista:'))
    l1.append(n)

def degrau(lista):
    l2=[]
    for i in range(0,len(lista)-1,1):
        df=abs(lista[i]-lista[i+1])
        l2.append(df)
    return l2

print(degrau(l1))
