# -*- coding: utf-8 -*-
from __future__ import division

p = int(input('Digite o valor de p:'))
q = int(input('Digite o valor de q:'))

contador=0
contadorp=0
contadorq=0
a=p

while a>0:
    a=a//10
    contadorp=contadorp+1
np=contadorp

b=q
while b>0:
    b=b+1
    contadorq=contadorq+1
nq=contadorq

if np<=nq:
    i=10**nq
    while q>0:
        if q%i==p:
            contador=contador+1
            break
        q=q//10
        
if contador>0:
    print ('S')
else:
    print ('N')
    
