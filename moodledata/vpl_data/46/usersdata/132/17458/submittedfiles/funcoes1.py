# -*- coding: utf-8 -*-
from __future__ import division

def crescente(lista):
    c=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            c=c+1
    if c==len(lista)-1:
        return True
    else:
        return False
#escreva as demais funções
def decrescente(lista):
    c=0
    for i in range(1,len(lista),1):
        if lista[i]<lista[i-1]:
            c=c+1
    if c==len(lista)-1:
        return True
    else:
        return False
def consecutivo(lista):
    c1=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            c1=c1+1
        if c1==0:
            print('N')
        else:
            print('S')
            



#escreva o programa principal
n=input('digite a quantidade de termos:')
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append(input('digite os termos de a:'))
if crescente(a):
    print('S')
else:
    print('N')
if decrescente(a):
    print('S')
else:
    print('N')