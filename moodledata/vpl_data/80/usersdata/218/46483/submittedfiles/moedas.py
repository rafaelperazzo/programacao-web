# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor a ser trocado:'))
i=0
cont=0
if a>=b:
    M=a
    m=b
else:
    M=b
    m=a
while cont==0:
    nvalor=c-(M*i)
    if nvalor%m==0:
        cont=1
        if (M*i)>c:
            cont=2
    else:
        i=i+1
if cont==2:
    print('NÃO')
if cont==1:
    print(i)
    print(nvalor//m)
        
    
    
    