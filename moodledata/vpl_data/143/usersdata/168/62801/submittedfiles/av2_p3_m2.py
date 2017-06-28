# -*- coding: utf-8 -*-
n=int(input('Digite a qauntidade de termos: '))
lista=[]
for i in range (0,n,1):
    numero=int(input('Digite a quantidade de'))
    lista.append(numero)
def degrau(lista):
    l=[]
    for i in range (0, len(lista)-1,1):
        diferenca=abs(lista[i]-lista[i+1])
        l.append(diferenca)
    return 1
print(degrau(lista))    