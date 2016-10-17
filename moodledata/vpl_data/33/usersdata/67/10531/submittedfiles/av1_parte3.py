# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
n=input("Digite o valor de termos:")
i=0
m=3
j=1
k=1
soma=0
for l in range(1,n+1,1):
    if l%2==0:
        s=s-(j/(k*(m**i)))
    else:
        s=s+(j/(k*(m**i)))
    i=i+1
    k=k+2
    
    