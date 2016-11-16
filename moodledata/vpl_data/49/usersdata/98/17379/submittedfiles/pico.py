# -*- coding: utf-8 -*-
from __future__ import division

#def pico(lista):
    #CONTINUE...
     


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
a=[]
for i in range(0,n,1):
    a.append(input('Digite um valor: '))
    
posicao=0
for i in range(0,len(a)-1,1):
    if a[i]>a[i+1]:
        posicao=i
        break
print posicao
        