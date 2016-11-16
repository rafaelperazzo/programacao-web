# -*- coding: utf-8 -*-
from __future__ import division
def iguais(listaa,listab):
    i=0
    
    contador=0
    
    while (len(listaa)-1)>=i:
        if listaa[i] in listab:
            contador=contador+1
        i=i+1
    return contador
    
n=input('digite o numero de elementos do primeiro vetor:')
m=input('digite o numero de elementos do segundo vetor:')

x=1
y=1
a=[]
b=[]

while n>=x:
    a.append(input('digite os elementos do primeiro vetor:'))
    x=x+1
while m>=y:
    b.append(input('digite os elementos do segundo vetor:'))
    y=y+1
print(iguais(a,b))