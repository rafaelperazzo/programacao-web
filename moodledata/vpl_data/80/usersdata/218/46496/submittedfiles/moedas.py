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
nvalor=c-(a*i)    
while nvalor<c or cont==0:
    nvalor=c-(a*i)
    if nvalor%b==0:
        cont=1
i=i+1
if cont==1:
    print(i)
    print(nvalor//b)
else:
    print('NÃO')
   
    
    
    