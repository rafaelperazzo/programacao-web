# -*- coding: utf-8 -*-
from __future__ import division

b= int(input('Digite um valor: '))
x=b

cont=0
while x>=1:
    cont= cont+1
    x= x/10
    
soma=0
for i in range (0, cont, 1):
    soma= soma+(b%10)*(2**i)

print(soma)