# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desviop(lista):
    somadp1=0
    for i in range(0,len(lista),1):
        somadp1=somadp1+((lista[i]-media(lista))**2)/(len(lista)-1)
    desviop=(somadp1)**0,5
    return desviop
        

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=input('Digite n :')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('Digite o elemento: '))
for i in range(0,n,1):
    b.append(input('Digite o elemento: '))
desviopa=desviop(a)
desviopb=desviop(b)
meda=media(a)
medb=media(b)
print(meda)
print(desviopa)
print(medb)
print(desviopb)

