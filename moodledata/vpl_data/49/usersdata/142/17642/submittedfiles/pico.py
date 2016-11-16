# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    posicao=0
    for i in range (0,len(lista)-1,1):
        if lista[i]>=lista[i+1]:
            posicao=i
            break
    contador=0
    for i in range (posicao,len(lista)-1,1):
        if lista[i]<=lista[i+1]:
            contador=contador+1
    if contador==0 and posicao!=0:
        return True
    else:
        return False
    #CONTINUE...
n = input('Digite a quantidade de elementos da lista: ')
a=[]
for i in range(0,n,1):
    a.append(input('Digite um valor:'))

if pico(a):
    print 'S'
else:
    print 'N'



#CONTINUE...

