# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
i=input('Digite o valor de i: ')
j=input('Digite o valor de j: ')
cont=0
k=1

while True:
    if j//k==0 and i//k==0:
        c=k
    
    if k==j or k==i:
        break
    k=k+1
print(c)