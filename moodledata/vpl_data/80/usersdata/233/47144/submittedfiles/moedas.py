# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor da cédula: '))
cont=0
if b<a:
    qb=c//b
    if (c%b)%a==0:
        qa=(c%b)/a
        print(qa)
        print(qb)
    elif (c%b)%a!=0:
        while (c%b)%a<1:
            for i in range(1,b+1,1):
                qb=(c//b)-i
                j=qb*b
                z=c-j
                qa=z/a
                if (c%b)%a==0 or (c%b)%a>=1:
                    break
            if (c%b)%a==0:   
                print(qa)
                print(qb)
            elif (c%b)%a>=1:
                print('N')

        
        
    
