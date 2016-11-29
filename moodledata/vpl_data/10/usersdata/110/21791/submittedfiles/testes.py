# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+a[i]
    med=soma/len(lista)
    
    return med 

def multiplicacao1(x,y):
    soma=0
    medx=media(x)
    medy=media(y)
    for i in range(0,len(x),1):
        soma=soma+(x[i]-medx)*(y[i]-medy)
    return soma
def multiplicacao2(x,y):
    mult2= multiplicacao1(x,x)* multiplicacao1(y,y)
    return mult2
    
    
def person(x,y):
    p= multiplicacao1(x,y)/(multiplicacao1(x,x)*(multiplicacao1(y,y)**(0.5))
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

    