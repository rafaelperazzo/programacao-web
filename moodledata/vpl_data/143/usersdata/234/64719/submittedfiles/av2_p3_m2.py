# -*- coding: utf-8 -*-
n=int(input('n'))
lista=[]
for i on range(0,n,1):
    numero=int(input('n'))
    lista.append(numero)
def degrau(lista):
    a=[]
    for i in range(0,len(lista)-1,1):
        diferenca=abs(lista[i]-lista[i+1])
        a.append(diferenca)
    return a

print(degrau(lista))
