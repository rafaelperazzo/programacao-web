# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite a quantidade de elementos: ')
a = []
b = []

cont = 0

for i in range (0,n,1):
    a.append(input('Digite o elemento da lista: '))
      if i==0:
        if a[0]>a[i]:
            cont = cont + 1
        else:
            cont = cont + 0
for i in range (0,n,1):
    b.append(input('Digite o elemento da lista: '))    
    if i==0:
        if b[0]>b[i]:
            cont = cont + 1
        else:
            cont = cont + 0
    if i==0:
        if a[0]>a[i]:
            cont = cont + 1
        else:
            cont = cont + 0
            
if cont == 0:
    print ('N')
else:
    print ('S')        