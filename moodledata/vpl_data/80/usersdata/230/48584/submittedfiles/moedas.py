# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite valores de moedas de a: '))
b=int(input('Digite valores de moedas de b: '))
c=int(input('Digite valores de cédulas de c: '))
if c%a!=0 and c%b!=0:
    a=a*0
    b=b*0
    print('N')
else:
    soma=0
    i=a
    while c>=i:
        soma=soma+1
        i=i+a
    print(soma)
    somaB=0
    j=b
    resto=c%a
    while j<=resto:
        somaB=somaB+1
        j=j+b
    print(somaB)

    
        

    
    