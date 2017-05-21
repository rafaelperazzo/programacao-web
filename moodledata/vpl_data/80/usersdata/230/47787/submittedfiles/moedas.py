# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite valores de moedas de a: '))
b=int(input('Digite valores de moedas de b: '))
c=int(input('Digite valores de cédulas de c: '))
somaA=0
somaB=0
i=0
while c>0:
    if c>=a:
        restoA=c%a
        somaA=somaA+restoA
    if (c%a)>=b:
        restoB=c%a
        somaB=somaB+restoB+somaA
        i=i+1
print(somaA)
print(somaB)
    
        

    
    