# -*- coding: utf-8 -*-
n=int(input('n:'))
lista=[]
for i in range(0,n,1):
    numero=int(input('n:'))
    lista.append(numero)
def degrau(lista):
    l=[]
    for i in range(0,len(lista)-1,1):
        d=abs(lista[i]-lista[i+1])
    return(l)

print(degrau(lista))
