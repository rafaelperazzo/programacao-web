# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor da cédula: '))
i=0
cont=0
while cont==0:
    if a<b:
        nvalor=c-(a*i)
        if nvalor%b==0:
            print(i)
            print(nvalor/b)
            cont=1
        if (a*i)>c:
            cont=1
            print('N')
    if b<a:
        nvalor=c-(b*i)
        if nvalor%a==0:
            print(i)
            print(nvalor/a)
            cont=1
        if (b*i)>c:
            cont=1
            print('N')            
    i=i=1    