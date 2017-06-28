# -*- coding: utf-8 -*-
n=int(input('n: '))
lista=[]
for i in range(0,n,1):
    num=int(input('valores: ')
    lista.append(num)
def degrau(lista):
    l=[]
    for i in range(0,len(lista)-1,1):
        diferenca=abs(lista[i]-lista[i+1])
        l.append(diferenca)
    return l
print(degrau(lista))