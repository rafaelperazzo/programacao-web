# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n: '))
for termo in range (1,n+1,1):
    x = float (input('Digite o valor de x: '))
    y = float (input('Digite o valor de y: '))
    
    if x>=0 and y>=0 and ((x**2)+(y**2))<=1:
        print('SIM')
        
    else:
        print('NAO')

