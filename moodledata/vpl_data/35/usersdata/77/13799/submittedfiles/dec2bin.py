# -*- coding: utf-8 -*-
from __future__ import division

p=int(input('Digite o valor de p: '))
q=int(input('Digite o valor de q:'))

contadorp=0
contadorq=0

i=p

while i>0:
    i=i//10.0
    contadorp=contadorp+1
    
jp=contadorp

k=p
while k>0:
    k=k//10
    contadorq=contadorq+1
    
jq=contadorq

if jp<=jq:
    l=10**jp
    while q>0:
        if q%l==p:
            contador=contador+1
        q=q//10

if contador>0:
    print('S')
else:
    print('N')

