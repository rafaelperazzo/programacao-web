# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite um valor:'))
b=int(input('digite um valor:'))
c=int(input('digite um valor:'))
i=0
cont=0
while cont==0:
    nvalor=c-(a*i)
    if nvalor%b==0:
        print(i)
        print(nvalor//b)
        cont=1
    if (a*i)>c:
        cont=1
        print('N')
    i=i+1    
    
    
    


