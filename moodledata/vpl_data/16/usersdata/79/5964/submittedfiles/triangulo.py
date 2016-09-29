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
        
    elif  (a**2) > (b**2) + (c**2):
        print('Ob')
        
    elif (a**2) < (b**2) + (c**2):
        print('Ac')
        

    if a == b == c:
    print('Eq')
    
    elif b == c =! a:
    print('Is')
    
    elif a =! b =! c:
    print('Es')
    
else:
    print('N')

    
    


