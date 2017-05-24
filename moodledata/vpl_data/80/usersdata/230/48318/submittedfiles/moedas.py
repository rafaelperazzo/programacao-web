# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite valores de moedas de a: '))
b=int(input('Digite valores de moedas de b: '))
c=int(input('Digite valores de cédulas de c: '))
somaA=0
i=a
while c<=a:
    somaA=somaA+1
    i=i+1
print(somaA)
somaB=0
j=b
resto=c%a
while b<=resto:
    restoB=c%a
    somaB=somaB+1
    i=i+1
print(somaB)
    
        

    
    