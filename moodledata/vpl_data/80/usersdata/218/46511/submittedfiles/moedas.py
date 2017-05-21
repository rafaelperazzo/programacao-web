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
        print(i)
        print(nvalor//b)
        cont=1
    if (a*i)>c:
        cont=1
        print('N')
    i=i+1    
   

   
    
    
    