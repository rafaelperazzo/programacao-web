# -*- coding: utf-8 -*-
from __future__ import division

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

i = 0
soma = 0

while a<c:

    if a>=0 and b>=0 and c>=0:
            soma = soma + (c/a)
        
        print (i)
        
        i = i+1
    else:
        print("n")
    
while b<c:

    if a>=0 and b>=0 and c>=0:
            soma = soma + (c/b)
        
        print (i)
        
        i = i+1
    else:
        print("n")
        