# -*- coding: utf-8 -*-
from __future__ import division

n1 = input('Digite o primeiro número:')
n2 = input('Digite o segundo número:')
n3 = input('Digite o terceiro número:')

if (n1>=n2 and n1>=n3):
    print ('%.2f'% n1)
    
elif (n2>=n1 and n2>=n3):
    print ('%.2f'% n2)
    
else:
    print ('%.2f'% n3)
    


