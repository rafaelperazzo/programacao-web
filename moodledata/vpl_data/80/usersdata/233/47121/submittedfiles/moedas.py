# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor da cédula: '))
cont=0
for i in range(0,c+1,1):
    if b>a and c%a!=0:
        qb=(c//b)-i
        qa=((c%b)//a)+i
    if a>b and c%b!=0:
        qa=(c//a)-i
        qb=((c%a)//b)+i   
    if b*qb=a*qa==c:
        break
print(qa)
print(qb)
        
        
    
