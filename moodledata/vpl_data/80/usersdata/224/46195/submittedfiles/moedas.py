# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor de moeda a: '))
b=int(input('Digite o valor de moeda b: '))
c=int(input('Digite o valor de cédula c: '))
soma=0
while c>0:
 if c//a==0:
     soma= soma+(c//10)
     if c//10!=0:
         soma1=(c%a)//b
if (c%a)%b==0:
    print(soma)
    print(soma1)
else:
    print('N')