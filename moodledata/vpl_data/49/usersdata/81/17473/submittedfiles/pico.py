# -*- coding: utf-8 -*-
from __future__ import division







n = input('Digite a quantidade de elementos da lista: ')
a=[]

for i in range(0,n,1):
    a.append(input('Digite um valor de a:'))
    

posicao=0
for i in range(0,len(a)-1,1):
    if a[i]>a[i]+1:
        posicao=i
        break
cont=0    
for i in range(posicao,len(a)-1,1):
    if a[i]<=a[i+1]:
        cont=cont+1
        
if cont==0:
    print'S'
else:
    print'N'
        