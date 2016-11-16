# -*- coding: utf-8 -*-
from __future__ import division
def iguais(listaa,listab):
    i=0
    j=0
    parametro=0
    if len(listaa)<=len(listab):
        while (len(listaa)-1)>=i:
            if listaa[i] in listab:
                parametro=parametro+1
            i=i+1
    elif len(listab)<len(listaa):
        while (len(listab)-1)>=j:
            if listab[j] in listaa:
                parametro = parametro+1
            j=j+1
    if parametro > 0:
        print ('S')
    else:
        print('N')
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