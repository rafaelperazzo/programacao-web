# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+a[i]
    med=soma/len(lista)
    
    return med 

def multiplicacao(lista1,lista2):
    soma=0
    medx=media(lista1)
    medy=media(lista2)
    for i in range(0,len(lista1),1):
        soma=soma+(lista1-medx)*(lista2-medy)
    return soma
def person(lista1,lista2):
    p=(multiplicacao(lista1,lista2,med1,med2)/(multiplicacao(lista1,lista1,med1,med1)*multiplicacao(lista2,lista2,med2,med2))**0.5
    return p
n=input('Digite n: ')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('Digite um valor '))
for i in range(0,n,1):
    b.append(input('Digite um valor '))
per=person(a,b)
print(per)

    