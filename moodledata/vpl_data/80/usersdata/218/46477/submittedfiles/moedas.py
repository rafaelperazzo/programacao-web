# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor a ser trocado:'))
i=0
cont=0
while cont==0:
    nvalor=c-(a*i)
    if nvalor%b==0:
        cont=1
        if (a*i)>c:
            break
    else:
        i=i+1
if cont==0:
    print('NÃO')
else:
    print(i)
    print(nvalor//b)
        
    
    
    