# -*- coding: utf-8 -*-
from __future__ import division

def vidas(lista):
    x=input('Digite o valor de x:')
    y=input('Digite o valor de y:')
    if y>=x:
        soma=0
        for i in range(x,y+1,1):
            soma=soma+lista[x]
    else:
        soma=0
        for i in range(y,x+1,1):
            soma=soma+lista[y]
    resultado=soma
    return resultado
n=input('Digite o valor de n:')
a=[]
for i in range(0,n,1):
    a.append(input('Digite um elemento:'))
print(vidas(a))    