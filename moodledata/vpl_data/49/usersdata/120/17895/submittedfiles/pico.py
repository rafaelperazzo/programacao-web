# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
n=input('digite a quantidade de elementos:')
a=[]
for i in range(0,n,1):
    a,append(input('digite um elemento:'))
posicao=0
for i in range(0,len(a)-1,1):
    if a[i]>a[i+1]:
        posicao=i
        break
cont=0
for i in range(posição,len(a)-1,1):
    if a[i]<=a[i+1]:
        cont=cont+1
if cont==0:
    print ('S')
else:
    print ('N')
#Entrada
a=[]
n=int(input('digite n:'))
#processamento
for i in range(0,n,1):
    a.append(input('digite um elemento:'))
  
#saida
if pico(a):
    print('S')
else:
    print('N')
    