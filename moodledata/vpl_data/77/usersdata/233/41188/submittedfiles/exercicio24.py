# -*- coding: utf-8 -*-
import math
n1=int(input('Digite um número inteiro: '))
m=int(input('Digite um número inteiro: '))
if n1<0 and n2<0:
    n=-1*n
    m=-1*m
mdc=n
while n % mdc !=0 or m%mdc !=0:
    mdc=mdc-1
print(mdc)    
    
