# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrada

a = float(input('Digite o valor do lado "a": '))
b = float(input('Digite o valor do lado "b": '))
c = float(input('Digite o valor do lado "c": '))

#Processamento 

if a < b + c:
    print('S')
    
    if (a**2) == (b**2) + (c**2):
        print('Re')
        
    if  (a**2) > (b**2) + (c**2):
        print('Ob')
        
    if (a**2) < (b**2) + (c**2):
        print('Ac')
        
    if b == c != a:
    print('Is')
    
    if a != b != c:
    print('Es')
    
else:
    print('N')

    
    


