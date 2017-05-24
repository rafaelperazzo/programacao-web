# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor de c: '))
i=0
cont=0

while cont==0:
    x=c-(a*i)
    if x%b==0:
        print(i)
        print(x//b)
        cont=1
    if (a*i)>c:
        print('N')
        cont=1
    i=i+1
    
    
        
    
