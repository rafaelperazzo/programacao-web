# -*- coding: utf-8 -*-
j=int(input('j'))
lista=[]
for i in range(0,j,1):
    numero=int(input('j'))
    lista.append(numero)
def degrau(lista):
    h=[]
    for i in range(0,len(lista)-1,1):
        k=abs(lista[i]-lista[i+1])
        h.append(k)
        return h
print(degrau(lista))