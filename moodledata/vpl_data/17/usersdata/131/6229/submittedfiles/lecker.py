# -*- coding: utf-8 -*-
from __future__ import division
import math
n1=input('Digite o valor do primeiro numero: ')
n2=input('Digite o valor do segundo numero: ')
n3=input('digite o valor do terceiro numero: ')
n4=input('digite o valor do quarto numero: ')

if n1>n2:
    print('S')
    
elif (n2) > (n3) and (n2)>(n1):
    print('S')
    else:
        print('n')
elif (n3)>(n4) and (n3)>(n2):
    print('S')
    else:
        print('n)
elif (n4)>(n3):
    print('S')
    else:
        print('n')

else:
    print('N')
        
    